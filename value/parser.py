import json
from json import JSONEncoder

def value_dumps(obj):
    print(1)
    if isinstance(obj, tuple):
        print("t")
    return obj