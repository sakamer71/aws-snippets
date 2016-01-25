from boto3.session import Session

role = 'assume-devel'
account = '130430642076'
region = 'us-east-1'

session = Session()
stsc = session.client('sts')
role_arn = "arn:aws:iam::{0}:role/{1}".format(account,role)
tmp_credentials = stsc.assume_role(RoleArn=role_arn, RoleSessionName='steve')
conn =  Session( region_name=region,
                     aws_access_key_id=tmp_credentials['Credentials']['AccessKeyId'],
                     aws_secret_access_key=tmp_credentials['Credentials']['SecretAccessKey'],
                     aws_session_token=tmp_credentials['Credentials']['SessionToken'])

r = conn.resource('ec2')
allinst = r.instances.all()
for i in allinst:
    print "my instance is {}".format(i.id)


