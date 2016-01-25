import boto3
from pprint import pprint
cidr = '10.50.0.0/16'
client = boto3.client('ec2')
resource = boto3.resource('ec2')

def create_vpc(cidr):
    vpc = client.create_vpc(
        CidrBlock = cidr
    )
    return vpc




response = create_vpc(cidr)
pprint(response)
vpcid = response['Vpc']['VpcId']
print vpcid

