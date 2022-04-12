pragma solidity ^0.8.0;

import "../OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/ERC20.sol";

contract Burnable is ERC20 {
    event BurnToken(address addr, uint256 token);

    // 跟 transfer 原理类似
    function BurnFrom(address from, uint256 tokens) {}

    function Burnable(uint256 tokens) public returns (bool){
        require(tokens <= _balances[msg.sender]);
        _totalSupply = _totalSupply.sub(tokens);
        _balances[msg.sender] = _balances[msg.sender].sub(tokens);
        emit BurnToken(msg.sender, tokens);
        // 做一个销毁
        emit Transfer(msg.sender, address(0), tokens);
        return true;
    }
}
