import pytest
from brownie import accounts
from web3 import Web3

from utils.contract_helper import get_contract_abi, w3_client


@pytest.fixture()
def get_contract(request):
    param = request.param
    print('param is', param)
    abi = get_contract_abi(param['name'])
    assert bool(abi)
    address = Web3.toChecksumAddress(param['value'])
    contract = w3_client.eth.contract(address=address, abi=abi)
    return contract
