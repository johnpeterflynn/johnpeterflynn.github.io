#!/usr/bin/env python3
"""
Convert BibTeX file to Quartz-compatible Markdown for publications page.

Usage:
    python scripts/bib_to_markdown.py content/static/publications.bib

This script reads a .bib file and generates formatted Markdown output
that can be pasted into content/publications/index.md.

Requirements:
    pip install bibtexparser
"""

import sys
import re
from pathlib import Path

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    print("Please install bibtexparser: pip install bibtexparser")
    sys.exit(1)


def format_authors(authors_str: str, highlight_name: str = "John Flynn") -> str:
    """Format author list, bolding the specified name."""
    # Split by " and "
    authors = [a.strip() for a in authors_str.split(" and ")]
    formatted = []
    for author in authors:
        # Handle "Last, First" format
        if "," in author:
            parts = author.split(",")
            author = f"{parts[1].strip()} {parts[0].strip()}"

        # Bold the highlighted author
        if highlight_name.lower() in author.lower():
            formatted.append(f"**{author}**")
        else:
            formatted.append(author)

    return ", ".join(formatted)


def format_venue(entry: dict) -> str:
    """Format the publication venue."""
    if entry.get("journal"):
        venue = entry["journal"]
        if entry.get("volume"):
            venue += f", {entry['volume']}"
            if entry.get("number"):
                venue += f"({entry['number']})"
        return f"*{venue}*"
    elif entry.get("booktitle"):
        return f"*{entry['booktitle']}*"
    return ""


def format_links(entry: dict) -> str:
    """Generate links for paper, code, video, etc."""
    links = []

    if entry.get("url"):
        links.append(f"[Paper]({entry['url']})")
    if entry.get("doi"):
        links.append(f"[DOI](https://doi.org/{entry['doi']})")
    if entry.get("code"):
        links.append(f"[Code]({entry['code']})")
    if entry.get("video"):
        links.append(f"[Video]({entry['video']})")
    if entry.get("slides"):
        links.append(f"[Slides]({entry['slides']})")

    return " | ".join(links) if links else ""


def entry_to_markdown(entry: dict) -> str:
    """Convert a single BibTeX entry to Markdown."""
    lines = []

    # Title
    title = entry.get("title", "Untitled").strip("{}")
    lines.append(f"### {title}")

    # Authors
    if entry.get("author"):
        authors = format_authors(entry["author"])
        lines.append(authors)

    # Venue and year
    venue = format_venue(entry)
    year = entry.get("year", "")
    note = entry.get("note", "")

    venue_line = venue
    if note:
        venue_line += f" - **{note}**"
    if venue_line:
        lines.append(venue_line)

    # Links
    links = format_links(entry)
    if links:
        lines.append(links)

    # Abstract (as quote)
    if entry.get("abstract"):
        lines.append("")
        lines.append(f"> {entry['abstract']}")

    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def parse_bib_file(bib_path: str) -> list:
    """Parse BibTeX file and return list of entries."""
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode

    with open(bib_path, "r", encoding="utf-8") as f:
        bib_database = bibtexparser.load(f, parser=parser)

    return bib_database.entries


def group_by_year(entries: list) -> dict:
    """Group entries by year, sorted descending."""
    years = {}
    for entry in entries:
        year = entry.get("year", "Unknown")
        if year not in years:
            years[year] = []
        years[year].append(entry)

    # Sort years descending
    return dict(sorted(years.items(), key=lambda x: x[0], reverse=True))


def generate_markdown(bib_path: str) -> str:
    """Generate full Markdown output from BibTeX file."""
    entries = parse_bib_file(bib_path)
    grouped = group_by_year(entries)

    output = []
    output.append("---")
    output.append("title: Publications")
    output.append("---")
    output.append("")
    output.append("# Publications")
    output.append("")
    output.append("A complete list of my academic publications.")
    output.append("")

    for year, year_entries in grouped.items():
        output.append(f"## {year}")
        output.append("")
        for entry in year_entries:
            output.append(entry_to_markdown(entry))

    output.append("---")
    output.append("")
    output.append("*To cite my work, you can download the [BibTeX file](/static/publications.bib).*")

    return "\n".join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python bib_to_markdown.py <path_to_bib_file>")
        print("Example: python scripts/bib_to_markdown.py content/static/publications.bib")
        sys.exit(1)

    bib_path = sys.argv[1]

    if not Path(bib_path).exists():
        print(f"Error: File not found: {bib_path}")
        sys.exit(1)

    markdown = generate_markdown(bib_path)

    # Output to stdout (can be redirected to file)
    print(markdown)

    # Optionally write directly to publications/index.md
    if len(sys.argv) > 2 and sys.argv[2] == "--write":
        output_path = Path("content/publications/index.md")
        output_path.write_text(markdown, encoding="utf-8")
        print(f"\nWritten to {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
