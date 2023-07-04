import boto3

# Create session
session = boto3.Session()

# Create EC2 client
ec2_client = session.client('ec2')

def list_vpcs():
    # Get list of VPCs
    response = ec2_client.describe_vpcs()
    vpcs = response['Vpcs']

    vpc_list = []
    for vpc in vpcs:
        vpc_id = vpc['VpcId']
        vpc_cidr = vpc['CidrBlock']
        vpc_name = ""
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if tag['Key'] == 'Name':
                    vpc_name = tag['Value']
                    break
        vpc_list += [(vpc_id,vpc_cidr,vpc_name)]
    return vpc_list
        
# Call the function to list VPCs
vpc_list = list_vpcs()
# Print VPC information
print("Existing VPCs:")
for (vpc_id,vpc_cidr,vpc_name) in vpc_list:
    print("VPC ID:", vpc_id)
    print("CIDR Block:", vpc_cidr)
    print("Name:", vpc_name)
    print("-------------------------")
