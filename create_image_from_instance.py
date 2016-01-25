import boto3
ec2 = boto3.client('ec2')

instance_to_image = 'i-9870a22e'

ec2.create_image(
    InstanceId = instance_to_image,
    Name = 'SteveImage'
)