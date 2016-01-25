import boto3
import os
cwd = '/Users/kamer/Downloads/music/'
s3b = 'kamerbucket'
destpath = 'music/'
s3 = boto3.resource('s3')

files = os.listdir(cwd)
for song in files:
    print "Uploading song {} to {} bucket".format(song,s3b)
    data = open(cwd+song, 'rb')
    s3.Bucket(s3b).put_object(Key=destpath+song,Body=data)

for i in files:
    print i