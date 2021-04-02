class IncrementCoinsError:
    def __init__(self, data):
        self.status=data['status']
    
    def get(self):
        if self.status == 'invalid id':
            return "The ID passed in \"increment_coins\" was invalid: An account does not exist with that ID"
        elif self.status == 'too small or big coins':
            return "The amount of coins you passed is either too large or too small: The number must be from 0-999999999999999"
        else:
            return "An unknown error occured"
        
    def show(self):
        print(self.get())

class SetCoinsError:
    def __init__(self, data):
        self.status=data['status']
    
    def get(self):
        if self.status == 'invalid id':
            return "The ID passed in \"increment_coins\" was invalid: An account does not exist with that ID"
        elif self.status == 'too small or big coins':
            return "The amount of coins you passed is either too large or too small: The number must be from 0-999999999999999"
        else:
            return "An unknown error occured"
        
    def show(self):
        print(self.get())

class GetUserError:
    def __init__(self, data):
        self.status=data['status']
    
    def get(self):
        if self.status == 'invalid id':
            return "The ID passed in \"get_user\" was invalid: An account does not exist with that ID"
        else:
            return "An unknown error occured"
        
    def show(self):
        print(self.get())

class SetPackageError:
    def __init__(self, data, dashboard_url):
        self.status=data['status']
        self.dash=dashboard_url

    def get(self):
        dashboard=self.dash
        if self.status == 'invalid id':
            return "The ID passed in \"increment_coins\" was invalid: An account does not exist with that ID"
        elif self.status == 'invalid package':
            return f"The package you passed does not exist on {dashboard}"
        else:
            return "An unknown error occured"

    def show(self):
        print(self.get())

class ResetPackageError:
    def __init__(self, data):
        self.status=data['status']

    def get(self):
        if self.status == 'invalid id':
            return "The ID passed in \"increment_coins\" was invalid: An account does not exist with that ID"
        else:
            return "An unknown error occured"

    def show(self):
        print(self.get())

class SetResourcesError:
    def __init__(self, data):
        self.status=data['status']

    def get(self):
        if self.status == 'invalid id':
            return "The ID passed in \"increment_coins\" was invalid: An account does not exist with that ID"
        elif self.status in ['ram size', 'disk size', 'cpu size', 'server size']:
            return f"Your ram/disk/cpu/server amount is either too large or too small: The number must be from 0-999999999999999"

    def show(self):
        print(self.get())