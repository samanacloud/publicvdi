import boto3

# Read the variables from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Create function
def create_vpc():
    # Create session
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION
    )
    ec2_client = session.client('ec2')

    # Create the VPC using the provided values
    response = ec2_client.create_vpc(CidrBlock=CIDR_BLOCK)
    vpc_id = response['Vpc']['VpcId']

    # Assign tags to the VPC
    ec2_client.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': VPC_NAME}, {'Key': 'Tag', 'Value': TAG_NAME}])

    # Create the subnet within the VPC
    response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=SUBNET_CIDR, AvailabilityZone=AVAILABILITY_ZONE)
    subnet_id = response['Subnet']['SubnetId']
    return (vpc_id,subnet_id)

if __name__ == "__main__":
    (vpc_id,subnet_id) = create_vpc()

    print("VPC created successfully:")
    print("VPC ID:", vpc_id)
    print("Subnet ID:", subnet_id)


