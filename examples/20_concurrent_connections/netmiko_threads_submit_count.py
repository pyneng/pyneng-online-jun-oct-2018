from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler



def connect_ssh(device_dict, commands):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = {device_dict['ip']: []}
        for command in commands:
            result[device_dict['ip']].append(ssh.send_command(command))
    return result


def threads_conn(function, devices, limit=2, command=None):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [
            executor.submit(function, device, command) for device in devices
        ]
        for f in as_completed(future_ssh):
            all_results.append(f.result())
    return all_results


if __name__ == '__main__':
    devices = yaml.load(open('devices_all.yaml'))
    print('Количество устройств:', len(devices))
    commands = ['sh clock', 'sh arp', 'sh ip int br', 'sh ip route', 'sh run']
    for num_threads in range(1,6):
        print(' {} потоков '.format(num_threads).center(50, '#'))
        start_time = datetime.now()
        all_done = threads_conn(connect_ssh, devices, command=commands, limit=num_threads)
        print(datetime.now() - start_time)

