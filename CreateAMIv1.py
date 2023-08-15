import boto3

# Read the AWS credentials from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Read the instance details from instance_info.dat
with open("instance_info.dat", "r") as file:
    instance_info = file.read()
    exec(instance_info)

# Read the AMI details from ami_info.dat
with open("ami_info.dat", "r") as file:
    ami_info = file.read()
    exec(ami_info)

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)
ec2_client = session.client('ec2')

def create_ami_from_instance(ec2_client, instance_id, ami_name, ami_description, ami_display_name):
    """
    Create an AMI from a given EC2 instance.

    Parameters:
    - ec2_client: boto3 EC2 client.
    - instance_id: ID of the EC2 instance to create the AMI from.
    - ami_name: Name for the new AMI.
    - ami_description: Description for the new AMI.
    - ami_display_name: Display name for the AMI (used for the "Name" tag).

    Returns:
    - AMI ID of the created AMI.
    """
    response = ec2_client.create_image(
        InstanceId=instance_id,
        Name=ami_name,
        Description=ami_description,
        NoReboot=True  # This ensures the instance is not rebooted during the AMI creation process.
    )
    ami_id = response['ImageId']

    # Add the "Name" tag to the AMI
    ec2_client.create_tags(
        Resources=[ami_id],
        Tags=[
            {
                'Key': 'Name',
                'Value': ami_display_name
            }
        ]
    )

    return ami_id

if __name__ == "__main__":
    ami_id = create_ami_from_instance(ec2_client, INSTANCE_ID, AMI_NAME, AMI_DESCRIPTION, AMI_DISPLAY_NAME)
    print(f"AMI created successfully with ID: {ami_id}")
