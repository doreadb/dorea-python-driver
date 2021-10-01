import sys
import json

sys.path.append("..")

from dorea import *
from value import *

def main():

    print(json.dumps((1,2),default=value_dumps))

    # 尝试数据库连接 [Web Service 连接]
    # client = DoreaClient (
    #     ("127.0.0.1", 3451),    # 服务连接信息（Web Service）
    #     "DOREA@TEST"            # 服务器连接密码（Web Service）
    # )

    # db = client.open("default")
    # print(db.get("hello"))


if __name__ == "__main__":
    main()