# -*- coding: utf-8 -*-

users = ['nata', 'sergey', 'igor']

for username in users:
    password = input('Введите пароль для пользователя {}: '.format(username))
    while True:
        if len(password) < 8:#1
            print('Пароль слишком короткий')
        elif username in password:#1
            print('Пароль содержит имя пользователя')
        else:#3
            print('Пароль для пользователя {} установлен'.format(username))
            break
        password = input('Введите пароль еще раз: ')

print('#'*50)

