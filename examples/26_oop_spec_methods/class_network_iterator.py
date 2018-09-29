import ipaddress

class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]

    def __iter__(self):
        print('Вызываю __iter__')
        self._index = 0
        return self

    def __next__(self):
        print('Вызываю __next__')
        if self._index < len(self.addresses):
            current_address = self.addresses[self._index]
            self._index += 1
            return current_address
        else:
            raise StopIteration


net1 = Network('10.1.1.192/28')

for i in net1:
    print(i)

'''
Вызываю __iter__
Вызываю __next__
10.1.1.193
Вызываю __next__
10.1.1.194
Вызываю __next__
10.1.1.195
Вызываю __next__
10.1.1.196
Вызываю __next__
10.1.1.197
Вызываю __next__
10.1.1.198
Вызываю __next__
10.1.1.199
Вызываю __next__
10.1.1.200
Вызываю __next__
10.1.1.201
Вызываю __next__
10.1.1.202
Вызываю __next__
10.1.1.203
Вызываю __next__
10.1.1.204
Вызываю __next__
10.1.1.205
Вызываю __next__
10.1.1.206
Вызываю __next__
'''

net2_iter = iter(net1)
#Вызываю __iter__

print(net2_iter._index)
#0

for i in net2_iter:
    print(i)
'''
Вызываю __iter__
Вызываю __next__
10.1.1.193
Вызываю __next__
10.1.1.194
Вызываю __next__
10.1.1.195
Вызываю __next__
10.1.1.196
Вызываю __next__
10.1.1.197
Вызываю __next__
10.1.1.198
Вызываю __next__
10.1.1.199
Вызываю __next__
10.1.1.200
Вызываю __next__
10.1.1.201
Вызываю __next__
10.1.1.202
Вызываю __next__
10.1.1.203
Вызываю __next__
10.1.1.204
Вызываю __next__
10.1.1.205
Вызываю __next__
10.1.1.206
Вызываю __next__
'''
