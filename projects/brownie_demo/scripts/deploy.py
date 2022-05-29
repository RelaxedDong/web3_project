#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:17 PM
# @Author  : donghao
import os

from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # 添加accounts方式：
    # local推荐：
    account = get_account()

    # test、线上推荐：
    # account = accounts.load('donghao')
    # print(account)

    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)

    # account = accounts.add(config['wallets']['from_key'])
    simple_storage = SimpleStorage.deploy({"from": account})
    v = simple_storage.retrieve()
    transaction = simple_storage.store(666, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def main():
    # brownie run scripts/deploy.py

    print('brownie run!')
    deploy_simple_storage()

# brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=666
# https://ethereum.stackexchange.com/questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie
