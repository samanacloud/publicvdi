# Citrix License Expiration Check PowerShell Script

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This is a PowerShell script that allows you to check the expiration date of a license file. It provides a convenient way to determine the number of days remaining until the license expires and displays appropriate messages based on the remaining days.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Prerequisites

- Windows Server 2016 or above
- PowerShell 5.1 or above

## Installation

1. Clone the repository or download the script.
2. Open a PowerShell session.
3. Navigate to the directory where the script (`checklicense.ps1`) is located.

## Usage

Run the script by providing the path to the license file using the `-LicenseFilePath` parameter:

```powershell
.\checklicense.ps1 -LicenseFilePath "path/to/license/file.lic"
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

See the [LICENSE](LICENSE) file for details.

## Authors

- [jorgeroan](https://github.com/jorgeroan)