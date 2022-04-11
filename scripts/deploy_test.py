#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:17 PM
# @Author  : donghao
from brownie import accounts, SimpleStorage


def main():
    """
    Running 'scripts/deploy_test.py::main'...
    0x7EA4768607dc17fb9CfF6d4d7c3d2E3aDDb1ED8e
    Transaction sent: 0xa54cae745d229ea7fcc8cf8c19faa951afc6fdd2586f6bac5435c3c1ee325609
      Gas price: 20.0 gwei   Gas limit: 114381   Nonce: 0
      SimpleStorage.constructor confirmed   Block: 1   Gas used: 103983 (90.91%)
      SimpleStorage deployed at: 0xf59084dDbcCf922664ae77D05023Ea58763c74fC
    :return:
    """
    acct = accounts.at('0x07112Cb0369d50E908d9F3086FB9b236Af6e39B9')
    print(acct)
    mytest = SimpleStorage.deploy(
        {"from": acct}
    )
    print(mytest)


# brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=666
# https://ethereum.stackexchange.com/questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie
