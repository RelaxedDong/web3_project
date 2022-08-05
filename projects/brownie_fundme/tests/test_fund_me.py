#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/8/5 12:06 PM
# @Author  : donghao
import pytest
from brownie import network, accounts, exceptions

from scripts.helpful_scirpts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENT

from scripts.deploy import deploy_fund_me


def test_can_fund_and_with_draw():
    print('network.show_active()', network.show_active())
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_with_draw():
    # brownie test -s -k test_only_owner_with_draw --network development
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_account = accounts.add()
    print('bad_account', bad_account.address, bad_account.balance())
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_account})
