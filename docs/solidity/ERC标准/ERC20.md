文档：
https://learnblockchain.cn/docs/eips/eip-20.html#api-%E8%A7%84%E8%8C%83

需要实现的 Interface:

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/IERC20.sol

> Erc-20是一个基于以太坊（Ethereum）代币（Token）的接口标准（协议）。所有符合Erc-20标准的代币都能立即兼容以太坊钱包（几乎所有支持以太币的钱包，包括Jaxx、MEW、imToken等。

> Erc-20 代币是以太坊代币的子集，这些所有代币通过Erc-20标准能够让以太坊区块链上的其他智能合约和去中心化应用之间无缝交互。

```solidity
pragma solidity ^0.8.0;

interface IERC20 {
    // 所有的token数量，有些erc20可以挖的然后totalsupply会变动
    function totalSupply() external view returns (uint256);

    // 一个地址持有的token的数量
    function balanceOf(address account) external view returns (uint256);
    // msg.sender -> to 转 amount个token，返回bool
    // 会执行 Emits a {Transfer} event.
    function transfer(address to, uint256 amount) external returns (bool);
    
    // 获取 owner 授权给 spender 可使用的token数量
    function allowance(address owner, address spender) external view returns (uint256);
    // msg.sender -> spender 可使用amount个token
    function approve(address spender, uint256 amount) external returns (bool);
    
    // 转移token。有个隐藏概念：from_address 授权过给 msg.sender，花的是from_address授权给msg.sender的token.
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool);
    
    // transferFrom
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    // approve
    event Approval(address indexed owner, address indexed spender, uint256 value);

}
```
# brownie 使用
首先安装包管理：
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