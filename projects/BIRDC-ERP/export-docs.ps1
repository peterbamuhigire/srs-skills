# export-docs.ps1 -- Copy all .docx deliverables into export/
$ScriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$ExportDir  = Join-Path $ScriptDir 'export'
New-Item -ItemType Directory -Force -Path $ExportDir | Out-Null
Write-Host "Project   : $(Split-Path -Leaf $ScriptDir)"
Write-Host "Exporting : $ExportDir"
Write-Host ""
$docxFiles = Get-ChildItem -Path $ScriptDir -Recurse -Filter '*.docx' |
             Where-Object { $_.FullName -notlike "*\export\*" }
$count = 0
foreach ($f in $docxFiles) {
    $dest = Join-Path $ExportDir $f.Name
    if (Test-Path $dest) { Write-Host "  OVERWRITE: $($f.Name)" }
    else                 { Write-Host "  COPY:      $($f.Name)" }
    Copy-Item -Path $f.FullName -Destination $dest -Force
    $count++
}
Write-Host ""
Write-Host "Exported $count file(s) to $ExportDir"
