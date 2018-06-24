import re
from pprint import pprint

{'SW2': {'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L',
         'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9'}}

def parse_cdp(filename):
    result = {}

    with open(filename) as f:
        for line in f:
            if line.startswith('Device ID'):
                #Device ID: SW2
                neighbor = re.search(
                    'Device ID: (\S+)', line).group(1)
                result[neighbor] = {}
            elif line.startswith('  IP address:'):
                #  IP address: 10.1.1.2
                ip = re.search(
                    '  IP address: (?P<ip>\S+)', line).groupdict()
                result[neighbor].update(ip)
            elif line.startswith('Platform:'):
                #Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
                platform = re.search(
                    'Platform: (?P<platform>\S+ \S+),', line).groupdict()
                result[neighbor].update(platform)
            elif line.startswith('Cisco IOS Software'):
                #Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)
                ios = re.search(
                    'Cisco IOS Software, (?P<ios>.+), RELEASE', line).groupdict()
                result[neighbor].update(ios)

    return result

pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))
