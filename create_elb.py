import boto3
elb = boto3.client('elb')

def create_elb(name, protocol, elb_port, inst_port):
    response = elb.create_load_balancer(
        LoadBalancerName = name,
        Listeners = [
            {
                'Protocol' : protocol,
                'LoadBalancerPort' : elb_port,
                'InstanceProtocol' : protocol,
                'InstancePort' : inst_port,
            }
        ],
        AvailabilityZones=['us-east-1a'],
    )
    return response

print create_elb("MyELB","HTTP",80,80)
