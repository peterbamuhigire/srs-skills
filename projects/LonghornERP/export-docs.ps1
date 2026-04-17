# export-docs.ps1 - Copy all .docx deliverables into this project's export folder.
#
# Usage (run from the project root):
#   .\export-docs.ps1
#
# The script finds every .docx in the project tree, skipping the export folder
# itself to prevent recursive copies, and places flat copies in export.

$ScriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ExportDir  = Join-Path $ScriptDir "export"

New-Item -ItemType Directory -Force -Path $ExportDir | Out-Null

Write-Host "Project   : $(Split-Path -Leaf $ScriptDir)"
Write-Host "Exporting : $ExportDir"
Write-Host ""

$files = Get-ChildItem -Path $ScriptDir -Filter "*.docx" -Recurse `
    | Where-Object { $_.FullName -notlike "*\export\*" } `
    | Sort-Object Name

$count = 0
foreach ($f in $files) {
    $dest = Join-Path $ExportDir $f.Name
    # Handle filename collisions
    if (Test-Path $dest) {
        $base = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
        $ext  = $f.Extension
        $n = 2
        while (Test-Path (Join-Path $ExportDir "${base}_${n}${ext}")) { $n++ }
        $dest = Join-Path $ExportDir "${base}_${n}${ext}"
    }
    Copy-Item $f.FullName -Destination $dest
    Write-Host "  + $($f.Name)"
    $count++
}

Write-Host ""
Write-Host "Done - $count file(s) copied to export/"
