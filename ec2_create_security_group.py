## creates a security group and allows inbound 80 and 443 from everywhere

import boto3
from time import sleep
ec2 = boto3.resource('ec2')
groupname = 'allow_ssh_and_http'

sg = ec2.create_security_group(
    GroupName = groupname,
    Description = 'Allows inbound ssh and http from everywhere',
    #VpcId = vpc
)
print sg
sgid = sg.id
print sgid


def add_ingress(protocol, fromport, toport, cidr):
    ## adds ingress rules for an existing security group
    mysg = ec2.SecurityGroup(sgid)
    newsg = mysg.authorize_ingress(
    GroupName = groupname,
    IpProtocol = protocol,
    FromPort = fromport,
    ToPort = toport,
    CidrIp = cidr
)

## add inbound ssh rule
add_ingress('tcp', 22,22,'0.0.0.0/0')

## add inbound ssh rule
add_ingress('tcp', 80,80,'0.0.0.0/0')

