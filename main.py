import requests
import json
import time
import random

print("test")
def test():
    response = requests.get("https://blockchain.info/ru/ticker").text
    print(response)

test()