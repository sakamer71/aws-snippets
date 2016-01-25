#!/usr/bin/env python
import paramiko
#from paramiko.client import SSHClient
#hostkeys = paramiko.HostKeys()
#keypath = '/Users/kamer/.ssh/known_hosts'
#hostkeys.load(keypath)
#print hostkeys

target = '52.3.209.37'
user = 'ec2-user'
sshkey = 'AWSLAB.pem'

client = paramiko.client.SSHClient()
#paramiko.AutoAddPolicy()

#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()

#print x
client.connect(target,username=user,pkey=sshkey)
