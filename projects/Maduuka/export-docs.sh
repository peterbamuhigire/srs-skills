#!/usr/bin/env bash
# export-docs.sh -- Copy all .docx deliverables into export/
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_DIR="$SCRIPT_DIR/export"
mkdir -p "$EXPORT_DIR"
echo "Project   : $(basename "$SCRIPT_DIR")"
echo "Exporting : $EXPORT_DIR"
echo ""
count=0
while IFS= read -r -d '' f; do
    dest="$EXPORT_DIR/$(basename "$f")"
    if [ -f "$dest" ]; then
        echo "  OVERWRITE: $(basename "$f")"
    else
        echo "  COPY:      $(basename "$f")"
    fi
    cp "$f" "$dest"
    ((count++)) || true
done < <(find "$SCRIPT_DIR" -name "*.docx" -not -path "*/export/*" -print0)
echo ""
echo "Exported $count file(s) to $EXPORT_DIR"
