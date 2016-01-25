import boto3
import sys
resource = boto3.resource('ec2')
allinst = resource.instances.all()
rows = []
srows = []
rows.append(["Choice","Instance ID","Private IP","Public IP","Key", "Name Label"])
for enum,inst in enumerate(allinst):
    count = enum+1
    id = inst.id
    priv_ip = inst.private_ip_address
    pub_ip = inst.public_ip_address
    key = inst.key_name
    tags = inst.tags
    try:
        nametag = [ x['Value'] for x in tags if x['Key'] == 'Name'][0]
    except:
        nametag = None
    rows.append([count,id,priv_ip,pub_ip, key, nametag])

for row in rows:
    myrow = ''
    for val in row:
        print '{:<20}'.format(val),
        #print val, type(val)
        myrow += str('{:<10}'.format(val))
        #myrow += val
    myrow += '\n'
    print
    srows.append(myrow)
choice = ''
print len(rows)
print rows
print srows
while not (choice > 0 and choice <= len(rows)):
    choice = raw_input("Select host to ssh to: ")
    #print "you selected {}".format(choice)
    if choice.lower() == 'q':
        exit()
    if not choice.isdigit():
        print "You must select a number\n"
    else:
        choice = int(choice)
print "you chose {}".format(choice)
