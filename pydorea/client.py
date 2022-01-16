from typing import Any, Tuple

import requests
import doson4py as doson
from pydorea import auth


class DoreaClient(object):
    
    def __init__(self, addr: Tuple[str, int], account: Tuple[str, str]) -> None:

        url = "http://" + addr[0] + ":" + str(addr[1])

        self.account = auth.Account(account[0], account[1])

        token = self.account.get_token(url)

        if token == None: 
            raise ValueError("service password failed")

        self.__options = {
            "addr": addr,
            "token": token,
            "url": url
        }

    def ping(self):

        try:
            r = requests.post (
                self.__options["url"] + "/ping",
                headers={ "Authorization": "Bearer " + self.__options["token"]["token"] }
            )
        except Exception:
            return False
        
        if r.status_code == 401:

            if r.json()["message"] == "token do not have access to this database.":
                raise ValueError("account no permission")

            new = self.account.get_token(self.__options["url"])
            
            if new != None:
                self.__options['token'] = new
                return self.ping()

        if r.status_code != 200:
            return False
        if r.json()['alpha'] == "OK":
            return True
        return False

    def open(self, name: str):
        if not self.ping():
            raise Exception("server connection failed")
        return DoreaGroup(self.__options, name, self.account)

class DoreaGroup(object):
    def __init__(self, options, name, account) -> None:
        
        self.__options = options
        self.name = name

        self.account = account

        self.__options["root"] = self.__options["url"]
        self.__options["url"] += "/@" + name

    def execute(self, command: str):

        r = requests.post (
            self.__options["url"] + "/execute",
            headers={ "Authorization": "Bearer " + self.__options["token"]["token"] },
            data={ "query": command }
        )
        
        if r.status_code == 401:

            if r.json()["message"] == "token do not have access to this database.":
                raise ValueError("account no permission")

            new = self.account.get_token(self.__options["root"])
            if new != None:
                self.__options['token'] = new
                return self.execute(command)
        return r.json()

    def get(self, key: str):
        
        result = self.execute("get {}".format(key))
        
        if result['alpha'] == "ERR":
            return None
        reply = result["data"]["reply"]
        return doson.loads(reply)
    
    def setex(self, key: str, value: Any, expire=0) -> bool:
        
        value = doson.dumps(value)

        code = "set {} {} {}".format(key, value, str(expire))
        result = self.execute(code)

        return result['alpha'] == "OK"
    
    def set(self, key: str, value: Any) -> bool:
        return self.setex(key, value, 0)

    def delete(self, key: str) -> bool:
        result = self.execute("delete {}".format(key))
        return result['alpha'] == "OK"

    def clean(self) -> bool:
        result = self.execute("clean")
        return result['alpha'] == "OK"