#!/usr/bin/env python3
"""Reject raw books and likely reconstructive full-text conversions."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


LARGE_BOOK_TEXT_BYTES = 80_000
RAW_BOOK_EXTENSIONS = {".epub", ".mobi", ".azw", ".azw3"}
SOURCE_TEXT_EXTENSIONS = {".md", ".txt", ".rst", ".html", ".htm"}
BOOK_SOURCE_PATH_RE = re.compile(
    r"(?:^|/)(?:book-extractions?|extracted-books?|book-dumps?|raw-books?|source-books?|book-study)(?:/|$)",
    re.IGNORECASE,
)
EXTRACTION_FILENAME_RE = re.compile(r"(?:-extractions?|books?-analysis)\.md$", re.IGNORECASE)
EXTRACTION_TARGET = r"(?:book-extractions?|extracted-books?|book-dumps?|raw-books?|source-books?|book-study)/"
# Markdown link targets into an extraction folder, e.g. [x](../../book-extractions/y.md).
EXTRACTION_LINK_RE = re.compile(r"\]\([^)\s]*" + EXTRACTION_TARGET + r"[^)\s]*\)", re.IGNORECASE)
# Backticked file paths inside an extraction folder, e.g. `book-extractions/y.md` (skills and root docs only).
EXTRACTION_CODE_PATH_RE = re.compile(r"`[^`\s]*" + EXTRACTION_TARGET + r"[^`\s]+\.md`", re.IGNORECASE)
LINK_SCAN_EXCLUDED_TOP = {"projects"}
FULL_TEXT_MARKERS = {
    "isbn": re.compile(r"\bISBN(?:-1[03])?\s*:?\s*[\dXx][\dXx\-\s]{8,}"),
    "copyright": re.compile(r"\bcopyright\s+(?:\u00a9|\(c\)|&copy;|[12]\d{3})", re.IGNORECASE),
    "rights-reserved": re.compile(r"\ball rights reserved\b", re.IGNORECASE),
    "reproduction-notice": re.compile(
        r"\bno part of this (?:book|publication|work) may be reproduced\b",
        re.IGNORECASE,
    ),
    "ebook-conversion": re.compile(
        r"(?:\[\]\{#[^}\n]*\.xhtml|calibre\d*|index_split_\d+\.html)",
        re.IGNORECASE,
    ),
}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", "node_modules"}


@dataclass(frozen=True)
class Finding:
    code: str
    path: Path
    message: str

    def format(self) -> str:
        return f"[ERROR] {self.code}: {self.path} {self.message}"


def _link_findings(path: Path, relative: Path, top: str) -> list[Finding]:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    found: list[Finding] = []
    match = EXTRACTION_LINK_RE.search(content)
    if match:
        found.append(
            Finding("book-extraction-link", relative, f"links to a book-extraction path: {match.group(0)}")
        )
    elif top != "docs":
        match = EXTRACTION_CODE_PATH_RE.search(content)
        if match:
            found.append(
                Finding("book-extraction-link", relative, f"references a book-extraction file: {match.group(0)}")
            )
    return found


def scan(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue

        suffix = path.suffix.lower()
        if suffix in RAW_BOOK_EXTENSIONS:
            findings.append(
                Finding(
                    "raw-book-source",
                    relative,
                    "raw ebook source files are temporary inputs and must not be stored in the repository",
                )
            )
            continue

        in_book_source_path = BOOK_SOURCE_PATH_RE.search(relative.as_posix()) is not None
        size = path.stat().st_size
        top = relative.parts[0] if relative.parts else ""
        if top not in LINK_SCAN_EXCLUDED_TOP:
            if in_book_source_path:
                findings.append(
                    Finding(
                        "book-extraction-folder",
                        relative,
                        "book extraction folders are not allowed; fold knowledge into skill references",
                    )
                )
            elif EXTRACTION_FILENAME_RE.search(path.name):
                findings.append(
                    Finding(
                        "book-extraction-file",
                        relative,
                        "extraction or book-analysis digests are not allowed; fold knowledge into skill references",
                    )
                )
            if suffix == ".md":
                findings.extend(_link_findings(path, relative, top))
        if suffix == ".pdf" and in_book_source_path:
            findings.append(
                Finding(
                    "raw-book-source",
                    relative,
                    "PDFs under book/source-extraction paths must stay outside the repository",
                )
            )
            continue
        if suffix not in SOURCE_TEXT_EXTENSIONS:
            continue

        if in_book_source_path and size >= LARGE_BOOK_TEXT_BYTES:
            findings.append(
                Finding(
                    "source-fulltext-path",
                    relative,
                    f"{size} bytes under a book-extraction path; retain concise synthesis, not source text",
                )
            )

        if size < 30_000:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        markers = sorted(name for name, pattern in FULL_TEXT_MARKERS.items() if pattern.search(content))
        if len(markers) >= 3:
            findings.append(
                Finding(
                    "source-fulltext-markers",
                    relative,
                    "likely reconstructive book text; matched markers: " + ", ".join(markers),
                )
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = scan(args.root)
    print(f"source-ingestion-guardrail: {args.root.resolve()}")
    print(f"findings: {len(findings)}")
    for finding in findings:
        print(finding.format())
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
