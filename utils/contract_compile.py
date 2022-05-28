#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/5/25 4:00 PM
# @Author  : donghao
from solcx import compile_standard, install_solc


# Install Solidity compiler.
_solc_version = "0.8.1"
install_solc(_solc_version)
with open("../contracts/基本语法/FirstAPP.sol") as f:
    content = f.read()
    # Compile SimpleStorage smart contract with solcx.
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
        # solc_version=_solc_version,
    )
    print(compiled_sol)
    # print( compiled_sol["contracts"])
    # abi = compiled_sol["contracts"]["SimpleStorage.sol"]["FirstAPP"]["abi"]
    # print(abi)