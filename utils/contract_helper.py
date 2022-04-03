#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2022/4/3 11:14 PM
# @Author  : donghao
import json
import pathlib


DEFAULT_ABI_JSON_FILE_PATH = '../build/contracts'


def get_contract_abi(contract_name: str, abi_dir=DEFAULT_ABI_JSON_FILE_PATH):
    current_dir = pathlib.Path(__file__).parent
    file_name = f"{contract_name}.json"
    file_full_name = pathlib.Path.joinpath(current_dir, abi_dir, file_name)
    with open(file_full_name) as f:
        abi_data = f.read()
        abi_json = json.loads(abi_data)
        if abi_json['contractName'] != contract_name:
            raise "合约名称不对应"
        return abi_json['abi']