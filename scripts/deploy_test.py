#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:17 PM
# @Author  : donghao
from brownie import accounts, SimpleStorage


def main():
    """
    (tornado_env) ☁  first_demo  brownie run scripts/deploy_test.py
    Brownie v1.18.1 - Python development framework for Ethereum

    FirstDemoProject is the active project.

    Running 'scripts/deploy_test.py::main'...
    0xa1eF58670368eCCB27EdC6609dea0fEFC5884f09
    (tornado_env) ☁  first_demo  brownie run scripts/deploy_test.py
    Brownie v1.18.1 - Python development framework for Ethereum

    FirstDemoProject is the active project.

    Running 'scripts/deploy_test.py::main'...
    0xa1eF58670368eCCB27EdC6609dea0fEFC5884f09
    Transaction sent: 0xb2477aefdbb15e8bcbb73b325fd57d2469bab143cb06d5193ad4581ff8b16b71
      Gas price: 2.0 gwei   Gas limit: 114381   Nonce: 3
      SimpleStorage.constructor confirmed   Block: 4   Gas used: 103983 (90.91%)
      SimpleStorage deployed at: 0xCe4A2940Be7f55041dEBF2473283b141c0872731
    :return:
    """

    acct = accounts.at('0xa1eF58670368eCCB27EdC6609dea0fEFC5884f09')
    print(acct)
    mytest = SimpleStorage.deploy(
        {"from": acct}
    )
    print(mytest)


# brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=666
# https://ethereum.stackexchange.com/questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie
