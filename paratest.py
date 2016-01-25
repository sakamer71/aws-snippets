import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())
ssh.connect('52.91.195.127', username='kamer', password='kamer')
#52.91.195.127
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls -liatr /')
print ssh_stdout
##!/usr/bin/env python
#import paramiko
'''
chan = ssh.get_transport().open_session()
chan.get_pty()
chan.invoke_shell()
chan.exec_command('hostname')
'''