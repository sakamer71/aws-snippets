import boto3
client = boto3.resource('s3')

data = open('listbuckets.py','rb')
client.Bucket('skamer-tamlab').put_object(Key='/testing/myfile.py', Body=data)