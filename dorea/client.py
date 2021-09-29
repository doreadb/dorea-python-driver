from typing import Tuple

import requests
from dorea import auth


class DoreaClient(object):
    def __init__(
        self, 
        addr: Tuple[str, int], 
        password: str,
        default_group = "default"
    ) -> None:

        url = "http://" + addr[0] + ":" + str(addr[1])

        token = auth.get_token(url, password)

        if token == None: 
            raise ValueError("service password failed")

        self.__options = {
            "addr": addr,
            "password": password,
            "token": token,
            "url": url
        }
        self.group = default_group

    def ping(self):

        r = requests.post (
            self.__options["url"] + "/ping",
            headers={ "Authorization": "Bearer " + self.__options["token"]["token"] }
        )
        
        if r.status_code != 200:
            return False
        if r.json()['alpha'] == "OK":
            return True
        return False

    def select(self, name):
        pass