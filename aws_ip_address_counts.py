## pulls down latest copy of AWS ip allocations and aggregates by service name

import requests
url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
r = requests.get(url)
data = r.json()
results = {}
for section in data['prefixes']:
    service = section['service']
    network = section['ip_prefix']
    subnet = int(network.split('/')[1])
    print network
    ipcount = 2**(32-subnet)
    #print service,network, subnet, ipcount
    if service not in results:
        results[service] = ipcount
    else:
        results[service] = results[service] + ipcount

for s in results:
    print '{:>20}'.format(s),
    print '{:>20}'.format(results[s])
    #print s,results[s]
