# Set Params
param(
    [string]$LicenseFilePath,
    [int]$Warning = 45,
    [int]$Critical = 30
)

# Verification of file and content
if (!(Test-path $LicenseFilePath)){
    Write-host "The specified license file does not exist."
    exit 2
}

$FileContent = Get-Content -Path $LicenseFilePath -Raw

if ($FileContent -notmatch '\d{4}\.\d{4}'){
    Write-host "The specified file is not a valid license file."
    exit 2
}

# Get expiration date
$datestring = (Get-Content -Path $LicenseFilePath | Select-String -Pattern '\d{4}\.\d{4}' | Select-Object -First 1).Matches.Value
$expire = [datetime]::ParseExact($datestring, 'yyyy.MMdd', $null)

# Calculate date
$daysRemaining = ($expire - (Get-Date)).Days

#Calculate expiration
if ($daysRemaining -lt 0) {
    Write-Host "CRITICAL: The license has expired."
} elseif ($daysRemaining -lt $Critical) {
    Write-Host "CRITICAL: The license will expire in $daysRemaining days."
} elseif ($daysRemaining -lt $Warning) {
    Write-Host "WARNING: The license will expire in $daysRemaining days."
} else {
    Write-Host "OK: The license will expire in $daysRemaining days."
}