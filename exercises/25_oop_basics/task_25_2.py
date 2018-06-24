# -*- coding: utf-8 -*-

'''
Задание 25.2

Создать класс CiscoSSH, который создает соединение SSH к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение SSH,
а также переход в режим enable.

Класс использует модуль netmiko для подключения по SSH.

Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Строки 'cisco' - это параметры username, password, enable_password.

После этого, должен быть доступен атрибут ssh, который ссылается на подключение к оборудованию:
In [3]: r1.ssh
Out[3]: <netmiko.cisco.cisco_ios.CiscoIosBase at 0xb34989ec>

Так как ssh является ссылкой на сессию SSH, которую создал netmiko, должны быть доступны и соответствующие методы netmiko:
In [4]: r1.ssh.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '


'''

import netmiko


