$WshShell = New-Object -comObject WScript.Shell
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$Shortcut = $WshShell.CreateShortcut("$DesktopPath\PrivateAI.lnk")
$Shortcut.TargetPath = "c:\Users\gamin\OneDrive\Desktop\private ai\PrivateAI\START_PRIVATEAI.bat"
$Shortcut.WorkingDirectory = "c:\Users\gamin\OneDrive\Desktop\private ai\PrivateAI"
$Shortcut.IconLocation = "shell32.dll,23"
$Shortcut.Save()
Write-Host "Shortcut created on Desktop successfully."
