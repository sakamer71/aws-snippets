import boto3
#from pprint import pprint
inst_id = ['i-6418cbd5']
ec2 = boto3.resource('ec2')
for i in inst_id:
    inst = ec2.Instance(i)
    response = inst.console_output()
    #pprint(response)
    print response['Output']