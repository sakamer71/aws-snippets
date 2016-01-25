## Deletes the most recent copy of a running instance with a specific AMI ID

import boto3
from datetime import datetime, timedelta
l = []
ec2 = boto3.resource('ec2')
ami = 'ami-60b6c60a'
instances = ec2.instances.filter(
    Filters = [{'Name':'image-id', 'Values':[ami]}, {'Name':'instance-state-name', 'Values':['running']}]
)
for i in instances:
    id = i.id
    lt = i.launch_time
    state = i.state
    print i.id, i.state
    now = datetime.now(lt.tzinfo)
    age = now-lt
    l.append([id,age])

print l
newest = min(x[1] for x in l)
oldest = max(x[1] for x in l)

instance_to_delete = [x[0] for x in l if x[1] == newest][0]
delete = ec2.instances.terminate(InstanceIds=[instance_to_delete])