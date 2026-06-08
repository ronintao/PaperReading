#!/usr/bin/env python3
"""Render a book-page range of a scanned PDF to PNGs, and probe the front-matter offset.

Scanned textbooks have a front-matter offset: the printed book page number differs from
the 0-based PDF page index. This script supports two modes:

  1) probe  — render a few low-dpi pages so you can read the printed page number and work
              out the offset (offset = pdf_index_1based - book_page).
  2) render — render an inclusive BOOK-page range to PNGs named by book page.

Dependencies: PyMuPDF (`pip install pymupdf`).

Examples
--------
Probe candidate PDF pages to discover the offset:
    python render_pages.py probe "book.pdf" --pdf-pages 225 236

Render book pages 218..229 once you know the offset is +12:
    python render_pages.py render "book.pdf" --book-range 218 229 --offset 12 -o temp_sec

Render by raw PDF indices instead (1-based), if you prefer:
    python render_pages.py render "book.pdf" --pdf-range 230 241 -o temp_sec
"""

import argparse
import os
import sys


def _open(pdf_path):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("PyMuPDF not installed. Run: pip install pymupdf")
    if not os.path.isfile(pdf_path):
        sys.exit(f"PDF not found: {pdf_path}")
    return fitz.open(pdf_path)


def cmd_probe(args):
    doc = _open(args.pdf)
    os.makedirs(args.out, exist_ok=True)
    print(f"page_count = {doc.page_count}")
    for p1 in args.pdf_pages:  # user gives 1-based PDF page numbers
        idx = p1 - 1
        if not (0 <= idx < doc.page_count):
            print(f"  skip pdf page {p1}: out of range")
            continue
        out = os.path.join(args.out, f"probe_pdf_{p1:03d}.png")
        doc[idx].get_pixmap(dpi=args.dpi).save(out)
        print(f"  wrote {out}")
    print("Read the probe images, note the printed book page number, then:")
    print("  offset = (1-based pdf page) - (printed book page)")


def cmd_render(args):
    doc = _open(args.pdf)
    os.makedirs(args.out, exist_ok=True)

    if args.book_range is not None:
        start, end = args.book_range
        if start > end:
            sys.exit("--book-range start must be <= end")
        pairs = [(bp, bp + args.offset - 1) for bp in range(start, end + 1)]
        name = lambda bp, idx: f"book_{bp:03d}.png"
    elif args.pdf_range is not None:
        start, end = args.pdf_range  # 1-based, inclusive
        if start > end:
            sys.exit("--pdf-range start must be <= end")
        pairs = [(p1, p1 - 1) for p1 in range(start, end + 1)]
        name = lambda p1, idx: f"pdf_{p1:03d}.png"
    else:
        sys.exit("Provide either --book-range (with --offset) or --pdf-range")

    written = 0
    for label, idx in pairs:
        if not (0 <= idx < doc.page_count):
            print(f"  skip {label}: pdf index {idx} out of range [0,{doc.page_count-1}]")
            continue
        out = os.path.join(args.out, name(label, idx))
        doc[idx].get_pixmap(dpi=args.dpi).save(out)
        written += 1
    print(f"wrote {written} page(s) to {args.out} at {args.dpi} dpi")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("probe", help="render a few pages low-dpi to discover the offset")
    p.add_argument("pdf")
    p.add_argument("--pdf-pages", type=int, nargs="+", required=True,
                   help="1-based PDF page numbers to probe, e.g. 225 236")
    p.add_argument("--dpi", type=int, default=120)
    p.add_argument("-o", "--out", default="temp_probe")
    p.set_defaults(func=cmd_probe)

    r = sub.add_parser("render", help="render an inclusive page range to PNGs")
    r.add_argument("pdf")
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--book-range", type=int, nargs=2, metavar=("START", "END"),
                   help="inclusive BOOK page range; needs --offset")
    g.add_argument("--pdf-range", type=int, nargs=2, metavar=("START", "END"),
                   help="inclusive 1-based PDF page range")
    r.add_argument("--offset", type=int, default=0,
                   help="offset = (1-based pdf page) - (book page); used with --book-range")
    r.add_argument("--dpi", type=int, default=200)
    r.add_argument("-o", "--out", default="temp_sec")
    r.set_defaults(func=cmd_render)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
