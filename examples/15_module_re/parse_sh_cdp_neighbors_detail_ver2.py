import re
from pprint import pprint


def parse_cdp(filename):
    regex = ('Device ID: (?P<device>\S+)'
             '|IP address: (?P<ip>\S+)'
             '|Platform: (?P<platform>\S+ \S+),'
             '|Cisco IOS Software, (?P<ios>.+), RELEASE')

    result = {}

    with open('sh_cdp_neighbors_sw1.txt') as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                name = match.lastgroup
                if name == 'device':
                    device = match.group(name)
                    result[device] = {}
                else:
                    result[device][name] = match.group(name)
    return result


pprint(parse_cdp('sh_cdp_neighbors_sw1.txt'))
