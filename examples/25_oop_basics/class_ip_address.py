

class IPAddress:
    def __init__(self, ipaddress):
        if not '/' in ipaddress:
            raise ValueError('IP адрес должен быть в формате X.X.X.X/MM')
        ip, mask = ipaddress.split('/')
        if not self._ip_is_correct(ip):
            raise ValueError('Неправильный IP адрес')
        self._ip = ip
        self._mask = int(mask)

    def bin(self):
        return ''.join('{:08b}'.format(int(i)) for i in self._ip.split('.'))

    def _ip_is_correct(self, ip):
        octets = ip.split('.')
        correct_octets = [octet for octet in octets
                          if octet.isdigit() and 1 <= int(octet) <= 255]
        if len(octets) == 4 and len(correct_octets) == 4:
            return True
        else:
            return False

