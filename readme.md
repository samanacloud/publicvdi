# AWS EC2 Automation Scripts

This repository contains Python scripts to automate common tasks on Amazon EC2, such as creating a VPC, launching EC2 instances, creating a custom AMI, etc.

## Included Scripts

### 1. `create_vpc.py`

This script creates a new VPC (Virtual Private Cloud) in your AWS account.

**Usage:**
```bash
python create_vpc.py

2. create_instance.py
This script launches a new EC2 instance in the specified VPC.

**Usage:**
```bash
python create_instance.py


## Create VPC Script

This script allows you to create a Virtual Private Cloud (VPC) in AWS using the provided configuration values. It utilizes the `boto3` library to interact with the AWS API.

### Prerequisites

Before running the script, ensure that you have the following:

- Python installed on your system
- `boto3` library installed (you can install it using `pip install boto3`)
- AWS credentials configured with appropriate permissions to create VPCs

### Installation

1. Clone the repository or download the script file.
2. Install the required dependencies by running `pip install boto3`.
3. Ensure that you have valid AWS credentials set up on your system.

###Configuration Files
The scripts read configuration from .dat files that must be present in the same directory as the scripts. These files contain information such as AWS credentials, resource IDs, etc.

info.dat: Contains AWS credentials and region information.
ami_info.dat: Contains information about the AMI to be created.
instance_info.dat: Contains information about the EC2 instance to be used.
launch_info.dat: Contains information for launching new EC2 instances.
infodelete.dat: Contains information about the resources that are intended to be deleted.
Note: Before running the scripts, make sure to update these .dat files with your own information.

Requirements
Python 3.x
Boto3 (Python SDK for AWS)
```

### Usage

Run the script using the command `python create_vpc.py`. The script will read the configuration values from `info.dat` and use them to create a VPC in your specified AWS region. After successful execution, the VPC ID and subnet ID will be displayed on the console.

### Example

```bash
$ python create_vpc.py
VPC created successfully:
VPC ID: vpc-12345678
Subnet ID: subnet-12345678
```

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or pull request.

### License

This script is licensed under the [MIT License](LICENSE).

### Acknowledgments

Special thanks to the developers and contributors of the `boto3` library for providing a seamless interface to interact with AWS services.

For more information, please refer to the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).