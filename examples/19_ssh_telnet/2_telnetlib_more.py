import telnetlib
import time


def send_command_telnetlib(ipaddress, username, password, enable_pass, command):
    t = telnetlib.Telnet('192.168.100.1')

    t.read_until(b'Username:')
    t.write(username.encode('utf-8') + b'\n')

    t.read_until(b'Password:')
    t.write(password.encode('utf-8') + b'\n')
    t.write(b'enable\n')

    t.read_until(b'Password:')
    t.write(enable_pass.encode('utf-8') + b'\n')

    t.read_until(b'#')

    t.write(command.encode('utf-8') + b'\n')
    result = ''

    while True:
        index, match, output = t.expect([b'--More--', b'#'], timeout=5)
        result += output.decode('utf-8')
        if index == 1:
            break
        t.write(b' ')
        time.sleep(1)

    return result


command = 'sh run'
user = password = enable_pass = 'cisco'
ip = '192.168.100.1'

print(send_command_telnetlib(ip, user, password, enable_pass, 'sh run'))

