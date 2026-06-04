param (
    [string]$Target = "backend",
    [switch]$Fix = $false
)

Write-Host "--- ECC Quality Gate ---" -ForegroundColor Cyan

# 1. Linting with Ruff
Write-Host "`n[1/3] Running Lint (Ruff)..." -ForegroundColor Yellow
if ($Fix) {
    python -m ruff check $Target --fix
} else {
    python -m ruff check $Target
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Lint failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Lint passed." -ForegroundColor Green

# 2. Type Checking (Placeholder for mypy if needed)
Write-Host "`n[2/3] Skipping Type Check (mypy not installed)..." -ForegroundColor Gray

# 3. Unit Tests with Pytest
Write-Host "`n[3/3] Running Tests (Pytest)..." -ForegroundColor Yellow
Set-Location $Target
python -m pytest
$testResult = $LASTEXITCODE
Set-Location ..

if ($testResult -ne 0) {
    Write-Host "❌ Tests failed!" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Tests passed." -ForegroundColor Green

Write-Host "`n🎉 Quality Gate Passed!" -ForegroundColor Cyan
exit 0
