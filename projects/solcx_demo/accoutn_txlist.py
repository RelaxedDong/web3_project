#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/6/7 11:24 AM
# @Author  : donghao
import requests

# params_tx = {
#     "apikey": "TF19NI54RAWK8G8M8V75EY83XPYZCEZKW9",
#     "module": "account",
#     "action": "txlist",
#     "address": "0x3Fef480B611d0adD76a4255f2aCEccbDb435E519",
#     "page": 1,
#     "sort": "asc",
#     "offset": 1,
# }
# i = 0
# response = requests.get('https://api-rinkeby.etherscan.io/api', params=params_tx)
# print(response.text)
result = {"status": "1", "message": "OK", "result": [{"blockNumber": "10338128", "timeStamp": "1647425921",
                                                      "hash": "0x496f39acd4760bb79167fd26f9a7ee703e80ffa45c3fa5fbb04968abae45c687",
                                                      "nonce": "1",
                                                      "blockHash": "0x93a018ff4015702aa7be560e937debb2c6a61c4ff58f9440cccbd396dc53b631",
                                                      "transactionIndex": "83",
                                                      "from": "0xac50925a3e7d26b76a8c5fc2fd5c7812bddf8518",
                                                      "to": "0x3fef480b611d0add76a4255f2aceccbdb435e519",
                                                      "value": "250000000000000000", "gas": "21000",
                                                      "gasPrice": "27083300000", "isError": "0",
                                                      "txreceipt_status": "1", "input": "0x", "contractAddress": "",
                                                      "cumulativeGasUsed": "15375062", "gasUsed": "21000",
                                                      "confirmations": "470124"}]}
constructor_arguments = result["result"][0]["input"]

print(constructor_arguments)
