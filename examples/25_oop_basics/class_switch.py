class Switch:
    def __init__(self, hostname, vendor):
        print('Run init method')
        self.hostname = hostname
        self.vendor = vendor

    def get_info(self):
        print('Switch {}, Vendor: {}'.format(self.hostname, self.vendor))



