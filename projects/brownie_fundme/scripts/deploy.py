#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/7/19 3:45 PM
# @Author  : donghao
from brownie import config, FundMe, network, MockV3Aggregator

from scripts.helpful_scirpts import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENT


def deploy_fund_me():
    current_network = network.show_active()
    account = get_account()
    if current_network not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config['networks'][current_network]['eth_use_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1]
    fund_me = FundMe.deploy(price_feed_address, {
        "from": account
    }, publish_source=config['networks'][current_network].get("verify"))
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    # brownie run scripts/deploy.py
    print('brownie run!')
    # brownie run scripts/deploy.py --network rinkeby
    deploy_fund_me()
