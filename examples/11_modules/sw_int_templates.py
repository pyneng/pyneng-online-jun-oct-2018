import os
import sys

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

l3int_template = ['no switchport', 'ip address']


def read_file_content(filename):
    if not os.path.exists(filename):
        return None
    with open(filename) as f:
        return f.read()

