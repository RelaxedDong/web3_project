#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/6/7 10:52 AM
# @Author  : donghao
import requests

data = {
    'apikey': 'TF19NI54RAWK8G8M8V75EY83XPYZCEZKW9',
    'module': 'contract',
    'action': "checkverifystatus",
    'guid': "xjjchmm4aqyuxl6zejvia84xueknsien9rmzfchssebv7faih5",
}

url = 'https://api-rinkeby.etherscan.io/api'
print("data is", data)
result = requests.post(url, data=data)
print(result.text)
