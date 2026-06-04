Write-Host "--- Gracia Autonoma: OpenRouter Setup ---" -ForegroundColor Cyan
$apiKey = Read-Host "Please enter your OpenRouter API Key"

if ([string]::IsNullOrWhiteSpace($apiKey)) {
    Write-Host "Error: API Key cannot be empty." -ForegroundColor Red
    exit 1
}

# Set environment variable for the current user permanently
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", $apiKey, "User")

Write-Host "Success! OPENROUTER_API_KEY has been set in your User Environment." -ForegroundColor Green
Write-Host "Please RESTART your terminal/IDE for the changes to take effect." -ForegroundColor Yellow
