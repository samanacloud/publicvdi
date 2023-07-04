import boto3

# Create session
session = boto3.Session()

# Create EC2 client
ec2_client = session.client('ec2')

def get_vpcs():
    # Get list of VPCs
    response = ec2_client.describe_vpcs()
    vpcs = response['Vpcs']

    # Print VPC information
    print("Existing VPCs:")
    for vpc in vpcs:
        vpc_id = vpc['VpcId']
        vpc_cidr = vpc['CidrBlock']
        vpc_name = ""
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if tag['Key'] == 'Name':
                    vpc_name = tag['Value']
                    break
        print("VPC ID:", vpc_id)
        print("CIDR Block:", vpc_cidr)
        print("Name:", vpc_name)
        print("-------------------------")

def delete_vpc(vpc_id):
    # Delete VPC
    try:
        response = ec2_client.delete_vpc(VpcId=vpc_id)
        print("VPC", vpc_id, "deleted successfully.")
    except Exception as e:
        print("Failed to delete VPC", vpc_id)
        print("Error:", str(e))

# Main function
def main():
    while True:
        print("1. Get existing VPCs")
        print("2. Delete a VPC")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            get_vpcs()
        elif choice == "2":
            vpc_id = input("Enter the VPC ID to delete: ")
            delete_vpc(vpc_id)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Print the VPC ID and Subnet ID from the first script
print("VPC ID:", vpc_id)
print("Subnet ID:", subnet_id)
