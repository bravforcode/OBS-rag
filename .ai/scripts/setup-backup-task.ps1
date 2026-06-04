$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "`"C:\Users\menum\Documents\ObsidianVault\Second Brain\.ai\scripts\vault-backup.py`" --incremental" -WorkingDirectory "C:\Users\menum\Documents\ObsidianVault\Second Brain"
$trigger = New-ScheduledTaskTrigger -Daily -At "22:00"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable:$false -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName "SecondBrain-DailyBackup" -Action $action -Trigger $trigger -Settings $settings -Description "Daily incremental backup of Second Brain vault" -Force
Write-Output "Scheduled task created: SecondBrain-DailyBackup at 22:00 daily"
