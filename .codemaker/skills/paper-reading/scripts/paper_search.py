#!/usr/bin/env python3
"""
PaperWiki Paper Search
Searches Semantic Scholar + arXiv for papers on a topic.
Usage:
  python paper_search.py --query "unified sequential recommendation transformer" \
                         --seeds HyFormer BST \
                         --venues KDD SIGIR WWW RecSys \
                         --limit 30 \
                         --download \
                         --out raw/new
"""

import argparse
import datetime
import json
import time
import os
import re
import sys
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

CURRENT_YEAR = datetime.datetime.now().year
DEFAULT_SINCE = CURRENT_YEAR - 2   # e.g. 2024 when running in 2026

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Paper:
    title: str
    authors: list[str]
    year: Optional[int]
    abstract: str
    venue: str
    citation_count: int
    s2_id: Optional[str] = None
    arxiv_id: Optional[str] = None
    pdf_url: Optional[str] = None
    source: str = ""          # "s2" | "arxiv" | "citation" | "reference"
    relevance_score: float = 0.0
    relevance_reason: str = ""

    def key(self) -> str:
        if self.s2_id:
            return self.s2_id
        if self.arxiv_id:
            return self.arxiv_id
        return self.title.lower()[:60]

# ---------------------------------------------------------------------------
# Semantic Scholar helpers
# ---------------------------------------------------------------------------

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,authors,year,abstract,venue,citationCount,externalIds,openAccessPdf"

def _s2_get(url: str, params: dict, retries: int = 5) -> dict:
    qs = urllib.parse.urlencode(params)
    full = f"{url}?{qs}"
    req = urllib.request.Request(full, headers={"User-Agent": "PaperWiki/1.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                # Exponential backoff: 10s, 20s, 40s, 80s, 160s
                wait = 10 * (2 ** attempt)
                print(f"  [S2] Rate limited (429), waiting {wait}s… (attempt {attempt+1}/{retries})", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  [S2] HTTP {e.code}: {full}", file=sys.stderr)
            return {}
        except Exception as e:
            print(f"  [S2] Error: {e}", file=sys.stderr)
            return {}
    print(f"  [S2] Gave up after {retries} retries: {full}", file=sys.stderr)
    return {}

def _parse_s2_paper(d: dict, source: str = "s2") -> Optional[Paper]:
    if not d.get("title"):
        return None
    ext = d.get("externalIds") or {}
    pdf_url = None
    if d.get("openAccessPdf"):
        pdf_url = d["openAccessPdf"].get("url")
    if not pdf_url and ext.get("ArXiv"):
        pdf_url = f"https://arxiv.org/pdf/{ext['ArXiv']}.pdf"
    return Paper(
        title=d["title"],
        authors=[a["name"] for a in (d.get("authors") or [])],
        year=d.get("year"),
        abstract=d.get("abstract") or "",
        venue=d.get("venue") or "",
        citation_count=d.get("citationCount") or 0,
        s2_id=d.get("paperId"),
        arxiv_id=ext.get("ArXiv"),
        pdf_url=pdf_url,
        source=source,
    )

def s2_search(query: str, limit: int = 20, since: Optional[int] = None) -> list[Paper]:
    print(f"[S2] Searching: {query!r}" + (f"  (since {since})" if since else ""))
    params: dict = {"query": query, "limit": limit, "fields": S2_FIELDS}
    if since:
        params["year"] = f"{since}-"   # S2 accepts "YYYY-" for "year >= YYYY"
    data = _s2_get(f"{S2_BASE}/paper/search", params)
    results = []
    for d in data.get("data") or []:
        p = _parse_s2_paper(d, "s2")
        if p:
            results.append(p)
    print(f"  → {len(results)} results")
    return results

def s2_paper_by_title(title: str) -> Optional[Paper]:
    data = _s2_get(f"{S2_BASE}/paper/search", {
        "query": title, "limit": 1, "fields": S2_FIELDS
    })
    items = data.get("data") or []
    if items:
        return _parse_s2_paper(items[0], "s2")
    return None

def s2_citations(paper_id: str, limit: int = 50) -> list[Paper]:
    """Papers that CITE this paper."""
    print(f"[S2] Fetching citations of {paper_id}")
    data = _s2_get(f"{S2_BASE}/paper/{paper_id}/citations", {
        "limit": limit,
        "fields": S2_FIELDS,
    })
    results = []
    for item in data.get("data") or []:
        d = item.get("citingPaper") or {}
        p = _parse_s2_paper(d, "citation")
        if p:
            results.append(p)
    print(f"  → {len(results)} citing papers")
    return results

def s2_references(paper_id: str, limit: int = 50) -> list[Paper]:
    """Papers that this paper CITES (its references)."""
    print(f"[S2] Fetching references of {paper_id}")
    data = _s2_get(f"{S2_BASE}/paper/{paper_id}/references", {
        "limit": limit,
        "fields": S2_FIELDS,
    })
    results = []
    for item in data.get("data") or []:
        d = item.get("citedPaper") or {}
        p = _parse_s2_paper(d, "reference")
        if p:
            results.append(p)
    print(f"  → {len(results)} references")
    return results

# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------

ARXIV_API = "http://export.arxiv.org/api/query"

def arxiv_search(query: str, limit: int = 20, since: Optional[int] = None) -> list[Paper]:
    date_suffix = ""
    if since:
        # arXiv date filter: submittedDate:[YYYYMMDD TO YYYYMMDD]
        date_suffix = f" AND submittedDate:[{since}0101 TO {CURRENT_YEAR}1231]"
    print(f"[arXiv] Searching: {query!r}" + (f"  (since {since})" if since else ""))
    params = {
        "search_query": f"all:{query}{date_suffix}",
        "start": 0,
        "max_results": limit,
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    qs = urllib.parse.urlencode(params)
    url = f"{ARXIV_API}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "PaperWiki/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            content = r.read().decode()
    except Exception as e:
        print(f"  [arXiv] Error: {e}", file=sys.stderr)
        return []

    results = []
    entries = re.findall(r"<entry>(.*?)</entry>", content, re.DOTALL)
    for entry in entries:
        title = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
        abstract = re.search(r"<summary>(.*?)</summary>", entry, re.DOTALL)
        arxiv_id_match = re.search(r"<id>.*?/abs/([^<]+)</id>", entry)
        authors_raw = re.findall(r"<name>(.*?)</name>", entry)
        year_match = re.search(r"<published>(\d{4})", entry)
        venue_match = re.search(r"<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>", entry, re.DOTALL)

        if not title or not arxiv_id_match:
            continue

        arxiv_id = arxiv_id_match.group(1).strip()
        p = Paper(
            title=title.group(1).strip().replace("\n", " "),
            authors=authors_raw,
            year=int(year_match.group(1)) if year_match else None,
            abstract=(abstract.group(1).strip() if abstract else ""),
            venue=venue_match.group(1).strip() if venue_match else "arXiv",
            citation_count=0,
            arxiv_id=arxiv_id,
            pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            source="arxiv",
        )
        results.append(p)

    print(f"  → {len(results)} results")
    return results

# ---------------------------------------------------------------------------
# Venue filter
# ---------------------------------------------------------------------------

VENUE_ALIASES = {
    "KDD": ["kdd", "knowledge discovery"],
    "SIGIR": ["sigir"],
    "WWW": ["www", "world wide web"],
    "RecSys": ["recsys", "recommender systems"],
    "WSDM": ["wsdm"],
    "CIKM": ["cikm"],
    "AAAI": ["aaai"],
    "IJCAI": ["ijcai"],
    "NeurIPS": ["neurips", "nips"],
    "ICML": ["icml"],
    "ICLR": ["iclr"],
    "arXiv": ["arxiv"],
}

def venue_match(paper: Paper, venues: list[str]) -> bool:
    if not venues:
        return True
    v = (paper.venue or "").lower()
    for target in venues:
        aliases = VENUE_ALIASES.get(target, [target.lower()])
        if any(a in v for a in aliases):
            return True
    # arXiv papers pass through unless strict venue list excludes them
    if paper.source == "arxiv" and "arXiv" in venues:
        return True
    return False

# ---------------------------------------------------------------------------
# Dedup + merge
# ---------------------------------------------------------------------------

def dedup(papers: list[Paper]) -> list[Paper]:
    seen: dict[str, Paper] = {}
    for p in papers:
        k = p.key()
        if k not in seen:
            seen[k] = p
        else:
            # keep higher citation count
            if p.citation_count > seen[k].citation_count:
                seen[k] = p
    return list(seen.values())

# ---------------------------------------------------------------------------
# Relevance scoring (heuristic)
# ---------------------------------------------------------------------------

def score_paper(paper: Paper, keywords: list[str], topic_context: str) -> tuple[float, str]:
    text = f"{paper.title} {paper.abstract}".lower()
    matched = [kw for kw in keywords if kw.lower() in text]
    base = len(matched) / max(len(keywords), 1)

    bonus = 0.0
    reasons = []

    if matched:
        reasons.append(f"matches keywords: {', '.join(matched)}")

    if paper.citation_count > 100:
        bonus += 0.15
        reasons.append(f"highly cited ({paper.citation_count})")
    elif paper.citation_count > 20:
        bonus += 0.05

    if paper.source in ("citation", "reference"):
        bonus += 0.1
        reasons.append("in citation graph of seed paper")

    score = min(base + bonus, 1.0)
    return round(score, 3), "; ".join(reasons) if reasons else "low keyword overlap"

# ---------------------------------------------------------------------------
# PDF download
# ---------------------------------------------------------------------------

def download_pdf(paper: Paper, out_dir: Path) -> Optional[Path]:
    if not paper.pdf_url:
        return None

    safe_title = re.sub(r"[^\w\s-]", "", paper.title)[:60].strip().replace(" ", "_")
    fname = f"{safe_title}.pdf"
    dest = out_dir / fname

    if dest.exists():
        print(f"  [skip] already exists: {fname}")
        return dest

    print(f"  [download] {fname}")
    try:
        req = urllib.request.Request(
            paper.pdf_url,
            headers={"User-Agent": "PaperWiki/1.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        if len(data) < 1000:
            print(f"    [warn] suspiciously small ({len(data)} bytes), skipping")
            return None
        dest.write_bytes(data)
        print(f"    saved ({len(data)//1024} KB)")
        time.sleep(1)
        return dest
    except Exception as e:
        print(f"    [error] {e}")
        return None

# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(
    papers: list[Paper],
    query: str,
    seeds: list[str],
    out_path: Path,
) -> None:
    papers_sorted = sorted(papers, key=lambda p: p.relevance_score, reverse=True)

    tier1 = [p for p in papers_sorted if p.relevance_score >= 0.6]
    tier2 = [p for p in papers_sorted if 0.3 <= p.relevance_score < 0.6]
    tier3 = [p for p in papers_sorted if p.relevance_score < 0.3]

    lines = [
        f"# PaperWiki Search Report",
        f"",
        f"**Query:** {query}",
        f"**Seeds:** {', '.join(seeds) if seeds else 'none'}",
        f"**Total candidates:** {len(papers)}",
        f"",
        f"## Tier 1 — Highly Relevant ({len(tier1)} papers, score ≥ 0.6)",
        "",
    ]
    for p in tier1:
        lines += _paper_entry(p)

    lines += [
        f"",
        f"## Tier 2 — Potentially Relevant ({len(tier2)} papers, 0.3–0.6)",
        "",
    ]
    for p in tier2:
        lines += _paper_entry(p)

    lines += [
        f"",
        f"## Tier 3 — Low Relevance ({len(tier3)} papers, score < 0.3)",
        "",
    ]
    for p in tier3:
        lines += _paper_entry(p)

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[report] saved → {out_path}")

def _paper_entry(p: Paper) -> list[str]:
    pdf_tag = f"[PDF]({p.pdf_url})" if p.pdf_url else "no PDF"
    return [
        f"### {p.title}",
        f"- **Authors:** {', '.join(p.authors[:3])}{'...' if len(p.authors)>3 else ''}",
        f"- **Year:** {p.year or '?'}  **Venue:** {p.venue or '?'}  **Citations:** {p.citation_count}",
        f"- **Source:** {p.source}  **Score:** {p.relevance_score}",
        f"- **Reason:** {p.relevance_reason}",
        f"- {pdf_tag}",
        f"- **Abstract:** {p.abstract[:600]}{'...' if len(p.abstract)>600 else ''}",
        "",
    ]

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_keywords(query: str) -> list[str]:
    stop = {"a","an","the","of","for","in","on","and","or","with","to","from","via","based","using"}
    words = [w.strip(".,") for w in query.split() if w.lower() not in stop and len(w) > 2]
    return words

def main():
    parser = argparse.ArgumentParser(description="PaperWiki Paper Search")
    parser.add_argument("--query", required=True, help="Search query string")
    parser.add_argument("--seeds", nargs="*", default=[], help="Seed paper titles/names to expand citation graph")
    parser.add_argument("--venues", nargs="*", default=[], help="Venue filter (e.g. KDD SIGIR WWW RecSys)")
    parser.add_argument("--limit", type=int, default=30, help="Max results per source")
    parser.add_argument("--download", action="store_true", help="Download PDFs to --out dir")
    parser.add_argument("--out", default="raw/new", help="Output dir for PDFs")
    parser.add_argument("--report", default="output/search_report.md", help="Report output path")
    parser.add_argument("--min-score", type=float, default=0.0, help="Min relevance score to download")
    parser.add_argument(
        "--since", type=int, default=DEFAULT_SINCE,
        help=f"Only include papers published >= this year (default: {DEFAULT_SINCE}, i.e. last 2 years). "
             f"Use --since 0 to disable the filter and search all years."
    )
    args = parser.parse_args()

    since = args.since if args.since > 0 else None

    out_dir = Path(args.out)
    report_path = Path(args.report)
    out_dir.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    keywords = build_keywords(args.query)
    print(f"Keywords: {keywords}")
    if since:
        print(f"Year filter: ≥ {since}  (pass --since 0 to disable)")
    else:
        print("Year filter: disabled (all years)")

    all_papers: list[Paper] = []

    # 1. Keyword search on Semantic Scholar (year filter passed to API)
    all_papers += s2_search(args.query, limit=args.limit, since=since)
    time.sleep(1)

    # 2. Keyword search on arXiv (date filter passed to API)
    all_papers += arxiv_search(args.query, limit=args.limit, since=since)
    time.sleep(1)

    # 3. Seed paper citation graph expansion
    #    Seeds are looked up without year filter (to find the seed itself regardless of age),
    #    but the citations/references returned are post-filtered below.
    for seed_title in args.seeds:
        print(f"\n[seed] Looking up: {seed_title!r}")
        seed = s2_paper_by_title(seed_title)
        time.sleep(0.5)
        if seed and seed.s2_id:
            print(f"  Found: {seed.title} (id={seed.s2_id})")
            all_papers += s2_citations(seed.s2_id, limit=50)
            time.sleep(1)
            all_papers += s2_references(seed.s2_id, limit=50)
            time.sleep(1)
        else:
            print(f"  [warn] seed not found: {seed_title}")

    # 4. Dedup
    all_papers = dedup(all_papers)
    print(f"\nAfter dedup: {len(all_papers)} unique papers")

    # 5. Year filter (post-fetch safety net — catches citation/reference results)
    if since:
        before = len(all_papers)
        all_papers = [p for p in all_papers if p.year is None or p.year >= since]
        print(f"After year filter (≥{since}): {len(all_papers)} (removed {before - len(all_papers)})")

    # 6. Venue filter
    if args.venues:
        before = len(all_papers)
        all_papers = [p for p in all_papers if venue_match(p, args.venues)]
        print(f"After venue filter {args.venues}: {len(all_papers)} (removed {before - len(all_papers)})")

    # 6. Score
    for p in all_papers:
        p.relevance_score, p.relevance_reason = score_paper(p, keywords, args.query)

    # 7. Report
    generate_report(all_papers, args.query, args.seeds, report_path)

    # 8. Download
    if args.download:
        to_download = [p for p in all_papers if p.relevance_score >= args.min_score and p.pdf_url]
        to_download.sort(key=lambda p: p.relevance_score, reverse=True)
        print(f"\n[download] {len(to_download)} papers to download → {out_dir}")
        for p in to_download:
            download_pdf(p, out_dir)

    # 9. Save JSON
    json_path = report_path.with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump([asdict(p) for p in all_papers], f, ensure_ascii=False, indent=2)
    print(f"[json] saved → {json_path}")

    print(f"\n✅ Done. {len(all_papers)} papers found.")
    tier1 = sum(1 for p in all_papers if p.relevance_score >= 0.6)
    print(f"   Tier 1 (≥0.6): {tier1}  Tier 2 (0.3-0.6): {sum(1 for p in all_papers if 0.3<=p.relevance_score<0.6)}  Tier 3 (<0.3): {sum(1 for p in all_papers if p.relevance_score<0.3)}")

if __name__ == "__main__":
    main()
