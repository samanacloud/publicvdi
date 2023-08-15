import boto3
import botocore
import time

# Read the variables from info.dat
with open("info.dat", "r") as file:
    info = file.read()
    exec(info)

# Read the variables from infodelete.dat
with open("infodelete.dat", "r") as file:
    info = file.read()
    exec(info)

# Create session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION
)
ec2_client = session.client('ec2')

# Terminate the instance
ec2_client.terminate_instances(InstanceIds=[INSTANCE_ID])
print("Instance terminated successfully.")

# Wait for the instance to shut down
print("Waiting for instance to shut down...")
time.sleep(120)  # Set desired time in seconds

# Delete the security group
ec2_client.delete_security_group(GroupId=SECURITY_GROUP_ID)
print("Security group deleted successfully.")

# Delete the EBS volume
try:
    ec2_client.delete_volume(VolumeId=VOLUME_ID)
    print("EBS volume deleted successfully.")
except botocore.exceptions.ClientError as e:
    if "InvalidVolume.NotFound" in str(e):
        print("The specified volume does not exist.")
    else:
        print("An error occurred:", e)



print("All resources deleted successfully.")
