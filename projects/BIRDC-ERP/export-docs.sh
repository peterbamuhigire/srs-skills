#!/usr/bin/env bash
# export-docs.sh — Copy all BIRDC ERP .docx files into export/ for client delivery
# Usage: bash export-docs.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_DIR="$SCRIPT_DIR/export"

mkdir -p "$EXPORT_DIR"

echo "Exporting BIRDC ERP documentation to $EXPORT_DIR ..."
echo ""

count=0
while IFS= read -r -d '' docx; do
    filename="$(basename "$docx")"
    cp "$docx" "$EXPORT_DIR/$filename"
    echo "  [OK] $filename"
    ((count++))
done < <(find "$SCRIPT_DIR" -name "*.docx" -not -path "*/export/*" -print0 | sort -z)

echo ""
echo "Export complete: $count documents copied to $EXPORT_DIR"
