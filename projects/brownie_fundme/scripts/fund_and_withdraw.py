#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/8/5 11:34 AM
# @Author  : donghao
from brownie import FundMe

from scripts.helpful_scirpts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"current entrance_fee is {entrance_fee}")
    print("fund......")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
