import netmiko


device_dict = {'device_type':'cisco_ios',
               'username': 'cisco',
               'password': 'cisco',
               'secret': 'cisco',
               'ip': '192.168.100.1' }


class CiscoSSH:

    def __init__(self, **device_dict):
        self.ssh = netmiko.ConnectHandler(**device_dict)
        self.ssh.enable()
        print('Вызываю __init__')

    def send_command(self, command):
        if not hasattr(self, 'show'):
            self.show = {}
        result = self.ssh.send_command(command)
        self.show[command] = result
        return result

    def __enter__(self):
        print('Вызываю __enter__')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Вызываю __exit__')
        print(exc_type, exc_value, traceback)
        self.ssh.disconnect()


with CiscoSSH(**device_dict) as r1:
    print(r1.send_command('sh clock'))
    raise ValueError('Возникла ошибка')

"""
Вызываю __init__
Вызываю __enter__
*08:45:39.770 UTC Sat May 19 2018
Вызываю __exit__
<class 'ValueError'> Возникла ошибка <traceback object at 0xb3d00f04>
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-22-5ba966fad127> in <module>()
      1 with CiscoSSH(**device_dict) as r1:
      2     print(r1.send_command('sh clock'))
----> 3     raise ValueError('Возникла ошибка')
      4

ValueError: Возникла ошибка
"""
