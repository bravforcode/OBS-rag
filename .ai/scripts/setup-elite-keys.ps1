Write-Host "--- Gracia Autonoma: Elite Free Stack Setup ---" -ForegroundColor Cyan
Write-Host "This script will help you set up Gemini (Google), Groq, and OpenRouter API keys." -ForegroundColor Gray

$googleKey = Read-Host "Please enter your GOOGLE_API_KEY (Gemini)"
$groqKey = Read-Host "Please enter your GROQ_API_KEY"
$openrouterKey = Read-Host "Please enter your OPENROUTER_API_KEY"

if ([string]::IsNullOrWhiteSpace($googleKey) -or [string]::IsNullOrWhiteSpace($groqKey) -or [string]::IsNullOrWhiteSpace($openrouterKey)) {
    Write-Host "Error: All API Keys must be provided." -ForegroundColor Red
    exit 1
}

# Set environment variables for the current user permanently
[Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", $googleKey, "User")
[Environment]::SetEnvironmentVariable("GROQ_API_KEY", $groqKey, "User")
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", $openrouterKey, "User")

Write-Host "Success! GOOGLE_API_KEY, GROQ_API_KEY, and OPENROUTER_API_KEY have been set in your User Environment." -ForegroundColor Green
Write-Host "Please RESTART your terminal/IDE for the changes to take effect." -ForegroundColor Yellow
