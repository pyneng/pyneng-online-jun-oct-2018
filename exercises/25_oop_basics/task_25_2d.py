# -*- coding: utf-8 -*-

'''
Задание 25.2d

Изменить метод send_cfg_commands из задания 25.2c и добавить в метод проверку на ошибки.

Метод должен обнаруживать ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении команды возникла ошибка, вывести сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

А также спросить у пользователя надо ли продолжать выполнять команды на этом устройстве.

Метод send_cfg_commands должен возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_cfg_commands:
In [3]: r1.send_cfg_commands(commands)
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка
-> Invalid input detected at '^' marker.
Продолжить выполнение команд? [y]/n y
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка
-> Incomplete command.
Продолжить выполнение команд? [y]/n n
Out[3]:
({},
 {'logging': 'logging\n% Incomplete command.\n\nR1(config)#',
  'logging 0255.255.1': "logging 0255.255.1\n                   ^\n% Invalid input detected at '^' marker.\n\nR1(config)#"})

'''

import netmiko

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors+correct_commands

