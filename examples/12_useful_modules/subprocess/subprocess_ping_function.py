import subprocess


def ping_ip(ip_address, verbose=False):
    '''
    Ping IP address and return tuple:
    On success:
        * True
    On failure:
        * False
    '''
    reply = subprocess.run(
        ['ping', '-c', '3', '-n', ip_address], encoding='utf-8',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if verbose:
        print(reply.stdout)
        print(reply.stderr)
    if reply.returncode == 0:
        return True
    else:
        return False


print(ping_ip('8.8.8.8', verbose=True))
print(ping_ip('a'))
