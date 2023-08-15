import boto3
import time

# Read the variables from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)
ec2_client = session.client('ec2')

def select_ami(ec2_client):
    # Select the AMI using the provided AMI ID
    response = ec2_client.describe_images(ImageIds=[AMI_ID])
    ami = response['Images'][0]
    return ami['ImageId']

def create_security_group(ec2_client, vpc_id):
    try:
        response = ec2_client.create_security_group(
            GroupName=SECURITY_GROUP_NAME,
            Description='Security group for my instance',
            VpcId=vpc_id
        )
        security_group_id = response['GroupId']

        # Add a rule that allows SSH traffic in on port 22 from your IP address
        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpProtocol='tcp',
            FromPort=22,
            ToPort=22,
            CidrIp=MY_IP_ADDRESS + '/32'
        )
    except ec2_client.exceptions.ClientError as e:
        if "InvalidGroup.Duplicate" in str(e):
            # If the security group already exists, get its ID
            response = ec2_client.describe_security_groups(
                Filters=[
                    {
                        'Name': 'group-name',
                        'Values': [SECURITY_GROUP_NAME]
                    },
                    {
                        'Name': 'vpc-id',
                        'Values': [vpc_id]
                    }
                ]
            )
            security_group_id = response['SecurityGroups'][0]['GroupId']
        else:
            raise e  # If the error is not due to a duplicate security group, raise the error

    return security_group_id


def create_instance(ec2_client, ami_id, subnet_id, security_group_id):
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,
        MaxCount=1,
        SubnetId=subnet_id,
        SecurityGroupIds=[security_group_id],
        KeyName=KEY_PAIR_NAME,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'VolumeSize': EBS_VOLUME_SIZE,
                    'VolumeType': EBS_VOLUME_TYPE,
                    'DeleteOnTermination': True
                }
            }
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': INSTANCE_NAME
                    }
                ]
            },
            {
                'ResourceType': 'volume',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': EBS_VOLUME_NAME
                    }
                ]
            }
        ]
    )
    instance_id = response['Instances'][0]['InstanceId']

    # Wait for the instance to be in 'running' state
    print("Waiting for instance to be in 'running' state...")
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

    # Describe the instance again to get the public IP
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    volume_id = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']

    return instance_id, volume_id, public_ip

if __name__ == "__main__":
    vpc_id = EXISTING_VPC_ID
    subnet_id = EXISTING_SUBNET_ID

    ami_id = select_ami(ec2_client)
    security_group_id = create_security_group(ec2_client, vpc_id)
    instance_id, volume_id, public_ip = create_instance(ec2_client, ami_id, subnet_id, security_group_id)

    print("Using existing VPC:")
    print("VPC ID:", vpc_id)
    print("Subnet ID:", subnet_id)
    print("Selected AMI ID:", ami_id)
    print("Security Group ID:", security_group_id)
    print("Instance ID:", instance_id)
    print("Volume ID:", volume_id)
    print("Instance Name:", INSTANCE_NAME)
    print("Public IP:", public_ip)

    # Write the connection information to a file
    with open("connection_info.txt", "w") as file:
        file.write(f"ssh -i id_rsa ubuntu@{public_ip}\n")


    # Write the details for deletion to infodelete.dat
    with open("infodelete.dat", "w") as file:
        file.write(f"INSTANCE_ID='{instance_id}'\n")
        file.write(f"SECURITY_GROUP_ID='{security_group_id}'\n")
        file.write(f"SUBNET_ID='{subnet_id}'\n")
        file.write(f"VPC_ID='{vpc_id}'\n")
        file.write(f"VOLUME_ID='{volume_id}'\n")

    
    # Write the instance information to instance_info.dat
    with open("instance_info.dat", "w") as file:
        file.write(f"INSTANCE_ID='{instance_id}'\n")
        file.write(f"VPC_ID='{vpc_id}'\n")
        file.write(f"SUBNET_ID='{subnet_id}'\n")
        file.write(f"SECURITY_GROUP_ID='{security_group_id}'\n")
        file.write(f"VOLUME_ID='{volume_id}'\n")
        file.write(f"PUBLIC_IP='{public_ip}'\n")