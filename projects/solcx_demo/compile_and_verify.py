#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/6/7 10:07 AM
# @Author  : donghao
import os

from web3 import Web3

abi = [
            {
                "inputs": [],
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            {
                "stateMutability": "payable",
                "type": "fallback"
            },
            {
                "inputs": [],
                "name": "implementation",
                "outputs": [
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "stateMutability": "payable",
                "type": "receive"
            }
        ]
bytecode = "60806040523480156200001157600080fd5b506040518060400160405280600b81526020017f6d657461667269656e64730000000000000000000000000000000000000000008152506040518060400160405280600281526020017f4d460000000000000000000000000000000000000000000000000000000000008152506040518060800160405280604d815260200162000c6e604d913960017f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbd60001c620000ca919062000654565b60001b7f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc60001b1462000126577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7380d39537860dc3677e9345706697bf4df6527f72620001747f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc60001b6200033660201b6200008f1760201c565b60000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550620002717380d39537860dc3677e9345706697bf4df6527f728484604051602401620001e3929190620005c5565b6040516020818303038152906040527f4cd88b76000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff83818316178352505050506200034060201b620000991760201c565b506200032c7380d39537860dc3677e9345706697bf4df6527f72826040516024016200029e9190620005a1565b6040516020818303038152906040527f30176e13000000000000000000000000000000000000000000000000000000007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19166020820180517bffffffffffffffffffffffffffffffffffffffffffffffffffffffff83818316178352505050506200034060201b620000991760201c565b505050506200075e565b6000819050919050565b60606200036e838360405180606001604052806027815260200162000cbb602791396200037660201b60201c565b905092915050565b606062000389846200045a60201b60201c565b620003cb576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401620003c29062000600565b60405180910390fd5b6000808573ffffffffffffffffffffffffffffffffffffffff1685604051620003f5919062000588565b600060405180830381855af49150503d806000811462000432576040519150601f19603f3d011682016040523d82523d6000602084013e62000437565b606091505b50915091506200044f8282866200047d60201b60201c565b925050509392505050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b606083156200048f57829050620004e2565b600083511115620004a35782518084602001fd5b816040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401620004d99190620005a1565b60405180910390fd5b9392505050565b6000620004f68262000622565b62000502818562000638565b93506200051481856020860162000699565b80840191505092915050565b60006200052d826200062d565b62000539818562000643565b93506200054b81856020860162000699565b6200055681620006fe565b840191505092915050565b60006200057060268362000643565b91506200057d826200070f565b604082019050919050565b6000620005968284620004e9565b915081905092915050565b60006020820190508181036000830152620005bd818462000520565b905092915050565b60006040820190508181036000830152620005e1818562000520565b90508181036020830152620005f7818462000520565b90509392505050565b600060208201905081810360008301526200061b8162000561565b9050919050565b600081519050919050565b600081519050919050565b600081905092915050565b600082825260208201905092915050565b600062000661826200068f565b91506200066e836200068f565b925082821015620006845762000683620006cf565b5b828203905092915050565b6000819050919050565b60005b83811015620006b95780820151818401526020810190506200069c565b83811115620006c9576000848401525b50505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000601f19601f8301169050919050565b7f416464726573733a2064656c65676174652063616c6c20746f206e6f6e2d636f60008201527f6e74726163740000000000000000000000000000000000000000000000000000602082015250565b610500806200076e6000396000f3fe6080604052600436106100225760003560e01c80635c60da1b1461003b57610031565b366100315761002f610066565b005b610039610066565b005b34801561004757600080fd5b50610050610080565b60405161005d919061034f565b60405180910390f35b61006e6100c6565b61007e6100796100c8565b61011f565b565b600061008a6100c8565b905090565b6000819050919050565b60606100be83836040518060600160405280602781526020016104a460279139610145565b905092915050565b565b60006100f67f360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc60001b61008f565b60000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b3660008037600080366000845af43d6000803e8060008114610140573d6000f35b3d6000fd5b606061015084610212565b61018f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101869061038c565b60405180910390fd5b6000808573ffffffffffffffffffffffffffffffffffffffff16856040516101b79190610338565b600060405180830381855af49150503d80600081146101f2576040519150601f19603f3d011682016040523d82523d6000602084013e6101f7565b606091505b5091509150610207828286610235565b925050509392505050565b6000808273ffffffffffffffffffffffffffffffffffffffff163b119050919050565b6060831561024557829050610295565b6000835111156102585782518084602001fd5b816040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028c919061036a565b60405180910390fd5b9392505050565b6102a5816103de565b82525050565b60006102b6826103ac565b6102c081856103c2565b93506102d0818560208601610410565b80840191505092915050565b60006102e7826103b7565b6102f181856103cd565b9350610301818560208601610410565b61030a81610443565b840191505092915050565b60006103226026836103cd565b915061032d82610454565b604082019050919050565b600061034482846102ab565b915081905092915050565b6000602082019050610364600083018461029c565b92915050565b6000602082019050818103600083015261038481846102dc565b905092915050565b600060208201905081810360008301526103a581610315565b9050919050565b600081519050919050565b600081519050919050565b600081905092915050565b600082825260208201905092915050565b60006103e9826103f0565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60005b8381101561042e578082015181840152602081019050610413565b8381111561043d576000848401525b50505050565b6000601f19601f8301169050919050565b7f416464726573733a2064656c65676174652063616c6c20746f206e6f6e2d636f60008201527f6e7472616374000000000000000000000000000000000000000000000000000060208201525056fe416464726573733a206c6f772d6c6576656c2064656c65676174652063616c6c206661696c6564a264697066735822122056f6e04cad3fc0bcbe4ac505e24b1fdab3199efc2fc70477ef19f2909453cd5a64736f6c63430008010033687474703a2f2f3132372e302e302e313a383030302f6170692f76312f6e6674676d2f6d657461646174612f72696e6b6562792f3632613139366135656236353839383233383963373438632f416464726573733a206c6f772d6c6576656c2064656c65676174652063616c6c206661696c6564"

# collect to ganache
w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/a047db24bb89483a87a1c1e8a136fa25'))
my_address = "0x3Fef480B611d0adD76a4255f2aCEccbDb435E519"
my_private_key = os.getenv("PRIVATE_KEY")
print(my_private_key)

myContract = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)
print("deploy contract...")
transaction = myContract.constructor().buildTransaction({"from": my_address,
                                                         "nonce": nonce,
                                                         "gasPrice": w3.eth.gas_price,
                                                         "chainId": 4})
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=my_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(tx_hash)
print("deployed!")
