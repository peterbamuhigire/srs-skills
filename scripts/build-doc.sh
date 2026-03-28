#!/usr/bin/env bash
# build-doc.sh — Stitch markdown section files and export to .docx via Pandoc
#
# Usage:
#   ./scripts/build-doc.sh <doc-dir> <output-name>
#
# Examples:
#   ./scripts/build-doc.sh projects/Livecare/02-requirements-engineering/01-srs SRS_Draft
#   ./scripts/build-doc.sh projects/Livecare/01-strategic-vision/01-prd PRD
#
# manifest.md format (optional, place in <doc-dir>):
#   List one filename per line. Lines starting with # are comments (excluded).
#   If absent, all *.md files in <doc-dir> are used, sorted alphabetically.

set -euo pipefail

DOC_DIR="${1:?Usage: build-doc.sh <doc-dir> <output-name>}"
OUTPUT_NAME="${2:?Usage: build-doc.sh <doc-dir> <output-name>}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="$SCRIPT_DIR/../templates/reference.docx"
PHASE_DIR="$(dirname "$DOC_DIR")"
OUTPUT_FILE="$PHASE_DIR/$OUTPUT_NAME.docx"

# Validate inputs
if [ ! -d "$DOC_DIR" ]; then
  echo "ERROR: Document directory not found: $DOC_DIR" >&2
  exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
  echo "ERROR: Reference template not found: $TEMPLATE" >&2
  echo "  Place a styled Word document at: $TEMPLATE" >&2
  exit 1
fi

# Resolve file list
if [ -f "$DOC_DIR/manifest.md" ]; then
  echo "Using manifest: $DOC_DIR/manifest.md"
  FILES=$(grep -v '^\s*#' "$DOC_DIR/manifest.md" | grep '\.md$' | sed "s|^|$DOC_DIR/|")
else
  echo "No manifest found — using alphabetical sort of *.md files"
  FILES=$(ls "$DOC_DIR"/*.md 2>/dev/null | grep -v 'manifest.md' | sort)
fi

if [ -z "$FILES" ]; then
  echo "ERROR: No .md files found in $DOC_DIR" >&2
  exit 1
fi

# Report what will be stitched
echo ""
echo "Stitching files:"
echo "$FILES" | while read -r f; do echo "  + $(basename "$f")"; done
echo ""

# Build
# -f markdown_github ensures GitHub Flavored Markdown rendering (consistent with
# how SKILL.md authors preview files on GitHub). Without this flag, Pandoc uses
# its own Markdown variant which differs in whitespace, footnote, and nested-list
# handling. (Etter, 2016 — Modern Technical Writing)
pandoc $FILES \
  -f gfm \
  --reference-doc="$TEMPLATE" \
  --table-of-contents \
  --toc-depth=3 \
  -o "$OUTPUT_FILE"

echo "Built: $OUTPUT_FILE"
