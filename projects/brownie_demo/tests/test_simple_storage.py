#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/5/29 10:05 PM
# @Author  : donghao
from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 0
    assert starting_value == expected_value


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(666, {"from": account})
    assert 666 == simple_storage.retrieve()

