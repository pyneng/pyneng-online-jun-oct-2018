def check_ip(ip_address):
   try:
       ipaddress.ip_address(ip_address)
       return True
   except ValueError:
       return False


def ip_is_unicast(ip_address):
    if check_ip(ip_address):
        ip = ipaddress.ip_address(ip_address)
        is_unicast = not ip.is_multicast and not ip.is_reserved and not ip.is_loopback
        #is_unicast = not (ip.is_multicast or ip.is_reserved or ip.is_loopback)
        return is_unicast
    raise ValueError('Неправильный формат IP адреса')



