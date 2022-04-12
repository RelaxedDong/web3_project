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
