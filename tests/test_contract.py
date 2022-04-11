#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 10:27 PM
# @Author  : donghao
import pytest

from utils.contract_helper import DEFAULT_ACCOUNT


@pytest.mark.parametrize(
    'get_contract',
    [{"name": "SimpleStorage", "value": "0xd62a1ecB2bafA2A963634FEfE2CbF5f54AbbBE0b"}],
    indirect=True
)
def test_hello(get_contract):
    print('get_contract is', get_contract)
    result = get_contract.functions.sayHello().call()
    assert result == 'hello, world'


@pytest.mark.parametrize(
    'get_contract',
    [{"name": "StateVariable", "value": "0x67056A947880bC3a91b422F714EA71AB66f9bDC7"}],
    indirect=True
)
def test_statevariable(get_contract):
    result = get_contract.functions.GetName().call({'from': DEFAULT_ACCOUNT})
    assert result == "unknown"
    result = get_contract.functions.SetName("donghao").call({'from': DEFAULT_ACCOUNT})
    assert result == "donghao"
    result = get_contract.functions.GetName().call()
    assert result == "donghao"
    # with brownie.reverts():
        # print('*'*100)
        # get_contract.functions.SetName("666").call({'from': "0x9429422a84F00e7b6f759de923704537f8b4723B"})

