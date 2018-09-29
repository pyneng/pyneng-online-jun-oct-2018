class CiscoSSH:

    def __init__(self, ip, username, password, enable):
        print('Подключаюсь к {}'.format(ip))
        device_dict = {'device_type':'cisco_ios',
                       'username': username,
                       'password': password,
                       'secret': enable,
                       'ip': ip }
        self.ssh = netmiko.ConnectHandler(**device_dict)
        self.ssh.enable()

    def send_command(self, command):
        result = self.ssh.send_command(command)
        return result

    def _get_display_str(self):
        ip = getattr(self.ssh, 'ip', None)
        user = getattr(self.ssh, 'username', None)
        return 'Hostname: {}, Model: {}'.format(ip, user)

    def connection_info(self):
        print(self._get_display_str())

