#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/5/29 11:18 PM
# @Author  : donghao
from brownie import SimpleStorage, accounts, config
from brownie.network.contract import ContractContainer, ProjectContract


def read_contract():
    # <brownie.network.contract.ContractContainer object at 0x11359ee80>
    # work same as array
    # >> 0x9c9B7F4D49572008c1717BE903A36B6641144A0a
    print(SimpleStorage[0])
    # >> brownie.network.contract.ProjectContract
    print(type(SimpleStorage[0]))


def main():
    read_contract()
