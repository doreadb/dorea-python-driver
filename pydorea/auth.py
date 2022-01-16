import requests

class Account(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_token(self, url: str):

        url = url + "/auth"

        try:
            result = requests.post(url=url, data={ 
                "username": self.username,
                "password": self.password,
            })
        except Exception:
            return None

        if result.status_code == 200:
            return result.json()["data"]
        return None