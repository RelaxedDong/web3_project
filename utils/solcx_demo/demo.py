#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/5/29 4:50 PM
# @Author  : donghao
import json
import os
from dotenv import load_dotenv
from solcx import compile_standard, install_solc
from web3 import Web3

load_dotenv()

with open("../../contracts/simplestorage_demo/SimpleStorage.sol") as f:
    content = f.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": content}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version=install_solc("0.8.0"),
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]['bytecode']['object']

# collect to ganache
chain_id = 1337
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
my_address = "0xf8Da8cAf800a1EcC1223b1F42459C5f655EC9F63"
my_private_key = os.getenv("PRIVATE_KEY")  # 45a5e0ade6a20b9331706ed6196b0e0b0ac4f48b5b83cfd1551f8b041888ad80

# create contract
SimpleStorageContract = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorageContract)

# get latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# 1. build transaction
# 2. sign transaction
# 3. send transaction
# build transaction
print("deploy contract...")
transaction = SimpleStorageContract.constructor().buildTransaction({"from": my_address,
                                                                    "nonce": nonce,
                                                                    "gasPrice": w3.eth.gas_price,
                                                                    "chainId": chain_id})
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=my_private_key)

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("deployed!")

# print(tx_hash)

# 等待交易执行完成
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# >> AttributeDict({'transactionHash': HexBytes('0x886f01615d9885d149140ff6900d6ea75fc5ac3d3c363d63a35868b78b0f4681'), 'transactionIndex': 0, 'blockHash': HexBytes('0xf22ba606b61d6fbac3cd6a47c12d0e52d6c2ef80f5375553f25c6b0afeaee048'), 'blockNumber': 2, 'from': '0xf8Da8cAf800a1EcC1223b1F42459C5f655EC9F63', 'to': None, 'gasUsed': 445051, 'cumulativeGasUsed': 445051, 'contractAddress': '0xFC5d9afEB74B418723C656b0D628afafA2B8556a', 'logs': [], 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
# print(tx_receipt)

# working with contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress,
                                 abi=abi)
# >> simple_storage.functions.retrieve(): <Function retrieve() bound to ()>
# print(simple_storage.functions.retrieve())

# .call() -> 调用函数并获取返回值，don't make a state change.
# .transact() -> make a state change

# print(simple_storage.functions.retrieve().call())
# 不会更改state， 调用retrieve还是返回0
# print(simple_storage.functions.store(123).call())

store_transaction = simple_storage.functions.store(666).buildTransaction({
    "from": my_address,
     "nonce": nonce+1,
     "gasPrice": w3.eth.gas_price,
     "chainId": chain_id
})
signed_txn = w3.eth.account.sign_transaction(store_transaction, private_key=my_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print(tx_receipt)
print(simple_storage.functions.retrieve().call())

