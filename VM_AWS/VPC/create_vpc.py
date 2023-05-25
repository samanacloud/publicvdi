# The Boto3 module, which provides the Python interface to interact with AWS services
import boto3

# Create function
def create_vpc():
    # AWS credentials
    aws_access_key_id = input("Enter AWS Access Key: ")
    aws_secret_access_key = input("Enter AWS Secret Key: ")
    aws_region = "us-west-1"  

    # Create session
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    # Check Credentials
    iam_client = session.client('iam')
    user = iam_client.get_user()

    if 'User' in user:
        print("AWS Credentials are valid.")
    else:
        print("AWS Credentials are invalid.")

create_vpc()
