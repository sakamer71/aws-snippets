import boto3
from pprint import pprint
r53 = boto3.client('route53')
response = r53.list_hosted_zones(

)
pprint(response)
zonename = response['HostedZones'][1]['Name']
zoneid = response['HostedZones'][1]['Id']
print zonename,zoneid

print "second try"
response = r53.get_hosted_zone(
    Id='/hostedzone/Z3KYFRZH3OEU05'
)
pprint(response)

