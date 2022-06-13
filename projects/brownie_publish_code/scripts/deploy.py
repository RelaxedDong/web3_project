#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:17 PM
# @Author  : donghao
import os

from brownie import accounts, config, NFT_GM, network


def deploy_simple_storage():
    # 添加accounts方式：
    # local推荐：
    account = get_account()
    NFT_GM.deploy({"from": account}, publish_source=True)



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
# https://ethereum.stackexchange.com    /questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie
