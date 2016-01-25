import boto3

ami = 'ami-60b6c60a'
type = 't2.nano'
sg = 'sg-fe9e9698'
subnet = 'subnet-14d8ca3f'
key = 'AWSLAB'
mincount = 1
maxcount = 1

client = boto3.client('ec2')
resource = boto3.resource('ec2')
response = client.run_instances(
ImageId = ami,
MinCount=mincount,
MaxCount=maxcount,
#SecurityGroupIds = [sg],
#SubnetId = subnet,
InstanceType = type,
KeyName = key,
NetworkInterfaces = [
    {
        'DeviceIndex':0,
        'AssociatePublicIpAddress':True,
        'SubnetId':subnet,
        'Groups':[sg],
    }
]
)

print "Waiting for launch of instance..."
instid =  response[u'Instances'][0]['InstanceId']
print response
print instid
waiter = client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instid])


i = resource.Instance(instid)
keyname = i.key_name
publicip = i.public_ip_address
state = i.state

print "Instance {} at {} is {} and key is {}".format(instid,publicip,state,keyname)

def terminate_instance(instancelist):
    print "Now terminating instances {}...".format(instancelist)
    client.terminate_instances(
        InstanceIds = instancelist
    )
    try:
        waiter = client.get_waiter('instance_terminated')
        waiter.wait(
            InstanceIds = instancelist
        )
        print "Instance {} terminated successfully".format(instancelist)
    except:
        print "Error - unable to terminate {}".format(instancelist)

terminate_instance([instid])
