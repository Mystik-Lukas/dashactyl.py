class DashactylUser:
    def __init__(self, jsondata):
        self.d = jsondata
    
    @property
    def package_ram(self):
        return self.d['package']['ram']

    @property
    def package_disk(self):
        return self.d['package']['disk']

    @property
    def package_cpu(self):
        return self.d['package']['cpu']

    @property
    def package_servers(self):
        return self.d['package']['servers']
    
    @property
    def extra_ram(self):
        return self.d['extra']['ram']

    @property
    def extra_disk(self):
        return self.d['extra']['disk']

    @property
    def extra_cpu(self):
        return self.d['extra']['cpu']

    @property
    def extra_servers(self):
        return self.d['extra']['servers']
    
    @property
    def coins(self):
        return self.d['coins']