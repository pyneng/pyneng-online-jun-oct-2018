from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


class CiscoSSH:
    def __init__(self, **device_dict):
        self.device_dict = device_dict

    def __call__(self, command):
        print(start_msg.format(datetime.now().time(), self.device_dict['ip']))
        self.ssh = ConnectHandler(**self.device_dict)
        self.ssh.enable()
        result = self.ssh.send_command(command)
        print(received_msg.format(datetime.now().time(), self.device_dict['ip']))
        return result


def threads_conn(devices, command, limit=2):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [
            executor.submit(device, command) for device in devices
        ]
        for f in as_completed(future_ssh):
            all_results.append(f.result())
    return all_results


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    dev_instances = [CiscoSSH(**params) for params in devices['routers']]
    all_done = threads_conn(dev_instances, command='sh clock')
    pprint(all_done)
