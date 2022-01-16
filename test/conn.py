import sys
import json

sys.path.append("..")

from pydorea import *

def main():

    # print(json.dumps((1,2),default=value_dumps))

    # 尝试数据库连接 [Web Service 连接]
    client = DoreaClient (
        ("127.0.0.1", 3451),    # 服务连接信息（Web Service）
        ("mrxiaozhuox", "123lze456")            # 服务器连接密码（Web Service）
    )
    # print(client.ping())
    db = client.open("mrxiaozhuox")
    print(db.get("foo"))
    # print(db.setex("hello", 3, 10))


if __name__ == "__main__":
    main()