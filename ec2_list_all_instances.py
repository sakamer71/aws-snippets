import boto3
from datetime import datetime, timedelta

ami = 'ami-60b6c60a'
ec2 = boto3.resource("ec2")

# vols = ec2.volumes
#
# for vol in vols:
#     print vol.id

instances = ec2.instances.filter(
    Filters = [{'Name':'image-id', 'Values':[ami]}]
)
for i in instances:
    id = i.id
    lt = i.launch_time
    now = datetime.now(lt.tzinfo)

    print id, lt, now, now-lt

# import boto3
# region = "us-east-1"
# ec2 = boto3.resource("ec2")
# def get_available_volumes():
#     available_volumes = ec2.volumes.filter(
#         Filters=[{'Name': 'status', 'Values': ['in-use']}]
#     )
#     return available_volumes
#
# vols = get_available_volumes()
# for vol in vols:
#     print vol.volume_id