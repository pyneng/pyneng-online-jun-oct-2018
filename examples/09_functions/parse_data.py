import os


def return_file_content(filename):
    if not os.path.exists(filename):
        print('Файла {} не существует'.format(filename))
        return None
    with open(filename) as f:
        return f.read()


def parse_sh_ip_int_br(command_output):
    intf_ip_dict = {}
    lines = command_output.split('\n')

    for line in lines:
        if line.count('.') == 3:
            intf, ip, *_ = line.split()
            intf_ip_dict[intf] = ip
            #print(intf, ip)
    return intf_ip_dict

content = return_file_content('sh_ip_int_br.txt')
print(parse_sh_ip_int_br(content))




'''
R1#show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  up                    down
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up
'''
