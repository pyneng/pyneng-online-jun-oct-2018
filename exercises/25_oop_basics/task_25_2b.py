# -*- coding: utf-8 -*-

'''
Задание 25.2b

Изменить класс CiscoSSH из задания 25.2a.

Добавить метод send_and_parse_show, который:
    1. отправляет команду show на оборудование
    2. получает результат
    3. парсит его с помощью TextFSM
    4. возвращает результат в виде списка словарей

Для отправки команды и получения ее результата должен использоваться метод send_show_command.

Шаблон TextFSM должен выбираться динамически, на основании команды.


Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_and_parse_show:
In [3]: r1.send_and_parse_show('sh ip int br')
Out[3]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

Использование метода send_and_parse_show с явным указанием всех параметров:
In [4]: r1.send_and_parse_show('sh ip int br', index_file='index', templates_dir='templates')
Out[4]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

'''

import netmiko


