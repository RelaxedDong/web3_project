官方文档： https://eth-brownie.readthedocs.io/en/latest/install.html

python3 -m pip install --user pipx

python3 -m pipx ensurepath

pipx install eth-brownie

依赖：

python3 version 3.6 or greater, python3-dev
ganache-cli(用于测试和开发的快速以太坊RPC客户端) - tested with version 6.12.2 

# 安装包管理
`brownie pm install OpenZeppelin/openzeppelin-contracts@4.5.0`

查看已安装包：
```bash
>> brownie pm list
Brownie v1.18.1 - Python development framework for Ethereum

The following packages are currently installed:

OpenZeppelin
 └─OpenZeppelin/openzeppelin-contracts@4.5.0
```
clone 到当前目录
```solidity
>> brownie pm clone OpenZeppelin/openzeppelin-contracts@4.5.0 
Brownie v1.18.1 - Python development framework for Ethereum

SUCCESS: Package 'OpenZeppelin/openzeppelin-contracts@4.5.0' was cloned at OpenZeppelin/openzeppelin-contracts@4.5.0
```

# 命令
```bash
  init               Initialize a new brownie project
  bake               Initialize from a brownie-mix template
  pm                 Install and manage external packages
  compile            Compile the contract source files
  console            Load the console
  test               Run test cases in the tests/ folder
  run                Run a script in the scripts/ folder
  accounts           Manage local accounts
  networks           Manage network settings
  gui                Load the GUI to view opcodes and test coverage
  analyze            Find security vulnerabilities using the MythX API
```
创建账户：
```shell
(tornado_env) ☁  brownie_demo [main] ⚡  brownie accounts new donghao
Brownie v1.18.1 - Python development framework for Ethereum

Enter the private key you wish to add: xxxb
Enter the password to encrypt this account with: 
SUCCESS: A new account 'xxxxxx' has been generated with the id 'donghao'


(tornado_env) ☁  brownie_demo [main] ⚡  brownie accounts list
Brownie v1.18.1 - Python development framework for Ethereum

Found 1 account:
 └─donghao: 0x6f31df378D40f5FD6305f7102fA5c1Cd2d720Bee

删除账户：
brownie accounts delete donghao
```

# test
可以参考：https://docs.pytest.org/


命令：`brownie test`

测试单个函数: `brownie test -k test_updating_storage`
测试单个文件: `brownie test -q test_class.py`

排查错误：`brownie test --pdb` 当有 error时，可以通过进入命令行查看对应的数据（相当于会断点到有error的那行代码）。

# console
`brownie console`

# import 
brownie无法识别npm安装的三方包