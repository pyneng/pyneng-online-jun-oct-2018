# -*- coding: utf-8 -*-

'''
Задание 26.3b

Изменить класс IPAddress из задания 26.3a.

В экземплярах классов есть не только строковое представление, но и, так называемое, "официальное" строковое представление. Это представление видно, когда мы отображаем объект ipython или когда объект отображается, например, в списке.

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

Строковое представление:
In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

Но, при этом, в таких случаях, строковое представление не используется:
In [8]: ip1
Out[8]: <__main__.IPAddress at 0xb44c37cc>

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [<__main__.IPAddress at 0xb44c37cc>]

In [12]: print(ip_list)
[<__main__.IPAddress object at 0xb44c37cc>]

In [13]: repr(ip1)
Out[13]: '<__main__.IPAddress object at 0xb44c37cc>'

За "официальное" представление объекта отвечает метод __repr__. И, чаще всего,
он отображает строку, скопировав которую, мы можем получить объект.

Пример вывода с настроенным методом __repr__:
In [15]: ip1 = IPAddress('10.1.1.1/24')

In [16]: ip1
Out[16]: IPAddress('10.1.1.1/24')

In [17]: ip_list = []

In [18]: ip_list.append(ip1)

In [19]: ip_list
Out[19]: [IPAddress('10.1.1.1/24')]

In [20]: print(ip_list)
[IPAddress('10.1.1.1/24')]

In [21]: repr(ip1)
Out[21]: "IPAddress('10.1.1.1/24')"


Сделать так, чтобы для экземпляров класса IPAddress, вывод метода __repr__ возвращался как в примерах выше.

'''

