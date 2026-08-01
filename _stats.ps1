$root = 'c:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full'
Get-ChildItem $root -Directory | ForEach-Object {
    $name = $_.Name
    $files = Get-ChildItem $_.FullName -Filter *.md
    $count = $files.Count
    $lines = 0
    foreach ($f in $files) {
        $lines += (Get-Content $f.FullName | Measure-Object -Line).Lines
    }
    Write-Output ("{0,-25} files={1,-4} lines={2}" -f $name, $count, $lines)
} | Sort-Object
