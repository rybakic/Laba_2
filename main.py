import requests
import json
import time
import random


def test():
    while True:
        response = requests.get("https://blockchain.info/ru/ticker").text
        d = json.loads(response)
        print(d[currency]['buy'])
        time.sleep(2)


currency = input()
test()