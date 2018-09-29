import netmiko


DEVICE_PARAMS = {
        'device_type': 'cisco_ios',
        'ip': '192.168.100.1',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'}


class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)


class CiscoRouter(CiscoSSH):
    pass


r1 = CiscoRouter(**DEVICE_PARAMS)
print(r1.send_show_command('sh clock'))

### Добавление метода

class CiscoRouter(CiscoSSH):
    def say_hello(self):
        print("Hello from {}".format(self.ssh.ip))


r1 = CiscoRouter(**DEVICE_PARAMS)
print(r1.say_hello())

### Переопределение родительского метода

class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

class CiscoRouter(CiscoSSH):
    def say_hello(self):
        print("Hello from {}".format(self.ssh.ip))

    def send_show_command(self, command):
        print('У меня тут командочка')
        command_result = CiscoSSH.send_show_command(self, command)
        return command_result

r1 = CiscoRouter(**DEVICE_PARAMS)
print(r1.send_show_command('sh ip int  br'))


### Варианты вызова родительского метода

class CiscoRouter(CiscoSSH):
    def say_hello(self):
        print("Hello from {}".format(self.ssh.ip))

    def send_show_command(self, command):
        print('У меня тут командочка')
        command_result = super().send_show_command(command)
        #command_result = super(CiscoRouter, self).send_show_command(command)
        #command_result = CiscoSSH.send_show_command(self, command)
        return command_result

### __init__ в дочернем классе

class CiscoRouter(CiscoSSH):
    def __init__(self, hostname, **device_params):
        self.hostname = hostname
        super().__init__(**device_params)

    def say_hello(self):
        print("Hello from {}".format(self.ssh.ip))

    def send_show_command(self, command):
        print('У меня тут командочка')
        command_result = super().send_show_command(command)
        return command_result

r1 = CiscoRouter('r1', **DEVICE_PARAMS)
print(r1.hostname)
print(r1.say_hello())

