import boto3

# AWS region
AWS_REGION = "us-west-2"

# Create function
def create_vpc(): 
    '''Que hace la funcion paso a paso y los parametros que retorna'''
    # Specify the AWS credentials
    aws_access_key_id = input("Enter AWS Access Key: ")
    aws_secret_access_key = input("Enter AWS Secret Key: ")

    # Create session
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=AWS_REGION
    )
    ec2_client = session.client('ec2')

    # Prompt the user for the necessary values
    cidr_block = input("Enter the VPC CIDR block (e.g., 10.0.0.0/16): ")
    vpc_name = input("Enter the VPC name: ")
    subnet_cidr = input("Enter the subnet CIDR block (e.g., 10.0.0.0/24): ")
    availability_zone = input("Enter the availability zone (e.g., us-west-1a): ")
    tag_name = input("Enter the tag name for the VPC: ")

    # Create the VPC using the provided values
    response = ec2_client.create_vpc(CidrBlock=cidr_block)
    vpc_id = response['Vpc']['VpcId']

    # Assign a name tag to the VPC
    ec2_client.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}, {'Key': 'Tag', 'Value': tag_name}])

    # Create the subnet within the VPC
    response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=subnet_cidr, AvailabilityZone=availability_zone)
    subnet_id = response['Subnet']['SubnetId']

    print("VPC created successfully:")
    print("VPC ID:", vpc_id)
    print("Subnet ID:", subnet_id)

if __name__ == "__main__":
    create_vpc()
