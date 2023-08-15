import boto3

# Read the AWS credentials from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Read the launch information from launch_info.dat
with open("launch_info.dat", "r") as file:
    launch_info = file.read()
    exec(launch_info)

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)
ec2_client = session.client('ec2')

def launch_instances_from_ami(ec2_client, ami_id, instance_type, key_pair_name, security_group_id, subnet_id, instance_count, instance_name_prefix):
    """
    Launch a specified number of EC2 instances from a given AMI.

    Returns:
    - List of instance IDs.
    """
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_pair_name,
        SecurityGroupIds=[security_group_id],
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=instance_count
    )
    
    instance_ids = [instance['InstanceId'] for instance in response['Instances']]
    
    # Assign the 'Name' tags to the launched instances
    for i, instance_id in enumerate(instance_ids, 1):
        ec2_client.create_tags(
            Resources=[instance_id],
            Tags=[{'Key': 'Name', 'Value': instance_name_prefix + str(i).zfill(3)}]
        )
    
    return instance_ids

if __name__ == "__main__":
    instance_ids = launch_instances_from_ami(ec2_client, AMI_ID, INSTANCE_TYPE, KEY_PAIR_NAME, SECURITY_GROUP_ID, SUBNET_ID, INSTANCE_COUNT, INSTANCE_NAME_PREFIX)
    
    # Write the instance IDs to a .txt file
    with open("created_instances.txt", "w") as file:
        for instance_id in instance_ids:
            file.write(instance_id + "\n")
    
    print(f"Launched instances: {', '.join(instance_ids)}")
    print(f"Instance IDs saved to created_instances.txt")
