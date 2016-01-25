import boto3
asg = boto3.client('autoscaling')

def create_launch_config(name, ami,inst_type, sshkey, sg):
    response = asg.create_launch_configuration(
        LaunchConfigurationName = name,
        ImageId = ami,
        KeyName = sshkey,
        SecurityGroups = sg,   ## list
        InstanceType = inst_type,
    )
    return response

create_launch_config('LaunchConfig1','ami-81034feb','t2.micro','AWSLAB', ['sg-4ce6d32a'])