#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:17 PM
# @Author  : donghao
from brownie import accounts, StateVariable


def main():
    acct = accounts.at('0x07112Cb0369d50E908d9F3086FB9b236Af6e39B9')
    print(acct)
    mytest = StateVariable.deploy({"from": acct})
    print(mytest)
