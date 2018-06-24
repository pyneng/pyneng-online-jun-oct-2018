# -*- coding: utf-8 -*-

'''
Задание 26.1a

Добавить к классу CiscoTelnet из задания 26.1 метод send_config_commands.

Метод принимает как аргумент список команд или одну команду (строку).

Метод send_config_commands должен переходить в конфигурационный режим,
отправлять команды и выходить из конфигурационного режима.

Метод должен возвращать вывод, который показывает ввод каждой команды.

In [1]: from task_26_1a import CiscoTelnet

In [2]: r1 = CiscoTelnet('192.168.100.1', 'cisco','cisco','cisco')

In [3]: print(r1.send_config_commands(['logging 10.1.1.1', 'logging 10.2.2.2']))
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.1.1.1
R1(config)#logging 10.2.2.2
R1(config)#end
R1#
'''


