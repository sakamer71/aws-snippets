import time
import os
import logging as log
def create_log():
    now = time.strftime("%m-%d-%Y")
    filename = 'testlog_' + now
    print filename
    log.basicConfig(filename=filename, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=log.DEBUG)
    log.info('*************************************************************************')
    log.info('Started...........')
    log.info('This file sucks:')
create_log()

for i in range(10):
    log.info('this is an info message')
    log.debug('this is a debug message')