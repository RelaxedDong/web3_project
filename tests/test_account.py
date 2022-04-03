#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:27 PM
# @Author  : donghao
import json
import pathlib

import pytest
from brownie import SimpleStorage, accounts
from web3 import Web3

from utils.contract_helper import get_contract_abi


@pytest.fixture
def token():
    return accounts[0].deploy(SimpleStorage)





def test_web3():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    assert w3.isConnected()
    abi = get_contract_abi("SimpleStorage")
    assert bool(abi)
    address = Web3.toChecksumAddress("0xce4a2940be7f55041debf2473283b141c0872731")
    contract = w3.eth.contract(address=address, abi=abi)
    result = contract.functions.sayHello().call()
    assert result == 'hello, world'
