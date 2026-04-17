#!/usr/bin/env bash
# export-docs.sh — Copy all .docx deliverables into this project's export/ folder.
#
# Usage (run from the project root or any subdirectory):
#   bash export-docs.sh
#
# The script finds every .docx in the project tree, skipping the export/ folder
# itself to prevent recursive copies, and places flat copies in export/.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_DIR="$SCRIPT_DIR/export"

mkdir -p "$EXPORT_DIR"

echo "Project : $(basename "$SCRIPT_DIR")"
echo "Exporting to : $EXPORT_DIR"
echo ""

count=0
while IFS= read -r -d '' f; do
    dest="$EXPORT_DIR/$(basename "$f")"
    # Handle filename collisions
    if [ -f "$dest" ]; then
        base="${f%.*}"
        ext="${f##*.}"
        n=2
        while [ -f "$EXPORT_DIR/$(basename "$base")_${n}.${ext}" ]; do n=$((n+1)); done
        dest="$EXPORT_DIR/$(basename "$base")_${n}.${ext}"
    fi
    cp "$f" "$dest"
    echo "  + $(basename "$f")"
    count=$((count + 1))
done < <(find "$SCRIPT_DIR" -name "*.docx" -not -path "*/export/*" -print0 | sort -z)

echo ""
echo "Done — $count file(s) copied to export/"
