function Start-Docker {
    # 1. Check if Docker engine is already running silently
    $dockerCheck = Start-Process docker -ArgumentList "ps" -WindowStyle Hidden -PassThru -Wait
    if ($dockerCheck.ExitCode -eq 0) {
        return
    }

    # 2. Start Docker Desktop if not running
    $dockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    
    if (Test-Path $dockerPath) {
        Start-Process $dockerPath -WindowStyle Hidden
    } else {
        return
    }
}

Start-Docker
