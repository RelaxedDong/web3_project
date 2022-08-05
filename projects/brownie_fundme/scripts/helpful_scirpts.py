#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/7/19 5:17 PM
# @Author  : donghao
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3


DECIMALS = 18
STARTING_PRICE = 2000 * 10 ** 8


LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        # deploy mocks
        print("current_network", network.show_active())
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed!")
