from typing import Tuple
from dorea import auth


class DoreaClient(object):
    def __init__(self, addr: Tuple[str, int], password: str) -> None:

        self.__options = {
            "addr": addr,
            "password": password
        }

        url = "http://" + addr[0] + ":" + str(addr[1])

        auth.get_token(url, password)