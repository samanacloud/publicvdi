import boto3

# Read the AWS credentials from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Read the instance IDs from created_instances.txt
with open("created_instances.txt", "r") as file:
    instance_ids = [line.strip() for line in file.readlines()]

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)
ec2_client = session.client('ec2')

def terminate_instances(ec2_client, instance_ids):
    """
    Terminate specified EC2 instances.

    Parameters:
    - ec2_client: boto3 EC2 client.
    - instance_ids: List of EC2 instance IDs to terminate.
    """
    response = ec2_client.terminate_instances(InstanceIds=instance_ids)
    terminated_instances = [instance['InstanceId'] for instance in response['TerminatingInstances']]
    return terminated_instances

if __name__ == "__main__":
    terminated_instances = terminate_instances(ec2_client, instance_ids)
    print(f"Terminated instances: {', '.join(terminated_instances)}")
