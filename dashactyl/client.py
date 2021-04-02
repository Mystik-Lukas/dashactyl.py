from .error import GetUserError, IncrementCoinsError, SetPackageError, ResetPackageError, SetResourcesError
from .dashboard.user import *
import json
import requests

class DashactylClient:
    def __init__(self, dashactyl_url, dashactyl_auth):
        self.url=dashactyl_url
        self.auth = dashactyl_auth

    def get_user(self, userid:int):
        try:
            data=requests.get(f"{self.url}/api/userinfo/?id={userid}", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" })
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] == 'success':
            return DashactylUser(data)
        error=GetUserError(data)
        error.show()
        return error

    def increment_coins(self, userid:int, amount:int):
        try:
            data=requests.get(f"{self.url}/api/userinfo/?id={userid}", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" })
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] == 'success':
            user=DashactylUser(data)
        else:
            user=GetUserError(data)
        if isinstance(user, GetUserError):
            error=IncrementCoinsError({'status': 'invalid id'})
            error.show()
            return error
        data = json.dumps({"id": str(userid), "coins": user.coins+amount})
        try:
            data=requests.post("https://dashboard.solarhost.club/api/setcoins", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" }, data=data)
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] != 'success': 
            error=IncrementCoinsError(data['status'])
            error.show()
            return error
        else:
            return True

    def set_package(self, userid:int, package:str):
        data = json.dumps({"id": str(userid), "package": package})
        try:
            data=requests.post("https://dashboard.solarhost.club/api/setplan", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" }, data=data)
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] != "success": 
            error=SetPackageError(data['status'], self.url)
            error.show()
            return error
        else:
            return True

    def reset_package(self, userid:int):
        data = json.dumps({"id": str(userid)})
        try:
            data=requests.post("https://dashboard.solarhost.club/api/setplan", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" }, data=data)
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] != "success": 
            error=ResetPackageError(data['status'])
            error.show()
            return error
        else:
            return True

    def set_resources(self, userid:int, ram:int=None, disk:int=None, cpu:int=None, servers:int=None):
        data = json.dumps({"id": str(userid), "ram": ram, "disk": disk, "cpu": cpu, "servers": servers})
        try:
            data=requests.post("https://dashboard.solarhost.club/api/setresources", headers={ "Content-Type": "application/json", "Authorization": f"Bearer {self.auth}" }, data=data)
        except:
            return print("Your dashactyl_url or dashactyl_auth is invalid")
        data=data.json()
        if data['status'] != "success": 
            error=SetResourcesError(data['status'])
            error.show()
            return error
        else:
            return True


    