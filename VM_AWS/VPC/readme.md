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

### Configuration

Edit the `info.dat` file and provide the necessary values for the AWS access key, secret access key, region, CIDR block, VPC name, subnet CIDR, and availability zone. Below is an example configuration:

```
AWS_ACCESS_KEY_ID = "AKIAYourAccessKeyID"
AWS_SECRET_ACCESS_KEY = "YourSecretAccessKey"
CIDR_BLOCK = "10.0.0.0/16"
VPC_NAME = "MyVPC"
SUBNET_CIDR = "10.0.0.0/24"
AVAILABILITY_ZONE = "us-west-1a"
TAG_NAME = "MyTag"
REGION = "us-west-2"
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