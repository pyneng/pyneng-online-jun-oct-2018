from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException

start_msg = '===> {} Connection to device: {}'
received_msg = '<=== {} Received result from device: {}'


def connect_ssh(device_dict, command):
    print(start_msg.format(datetime.now().time(), device_dict['ip']))
    if device_dict['ip'] == '192.168.100.1':
        time.sleep(10)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return (device_dict['ip'], result)


def print_done(future):
    ip, output = future.result()
    print(received_msg.format(datetime.now().time(), ip))
    print(output)
    return ip, output


def threads_conn(function, devices, command, limit=2, callback=None):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = []
        for device in devices:
            future = executor.submit(function, device, command='sh ip int br')
            if callback: future.add_done_callback(callback)
            futures.append(future)
        for f in as_completed(futures):
            all_results.append(f.result())
    return all_results


if __name__ == '__main__':
    devices = yaml.load(open('devices.yaml'))
    all_done = threads_conn(
        connect_ssh, devices, command='sh clock', callback=print_done)
    pprint(all_done)
