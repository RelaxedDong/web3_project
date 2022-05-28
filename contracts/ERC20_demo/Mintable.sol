pragma solidity ^0.8.0;

import "../OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/ERC20.sol";

contract Mintable is ERC20 {
    mapping(address => bool) minters;
    address private owner;
    constructor() public {
        owner = msg.sender;
    }
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    modifier onlyMinter() {
        require(minters[msg.sender]);
        _;
    }
    function addMinter(address addr) public onlyOwner returns (bool) {
        minters[addr] = true;
        return true;
    }

    function mint(address to, uint256 token) public onlyMinter returns (bool){
        // 增加total_supply
        // 转移新增出来的token到某个address
        _totalSupply = _totalSupply.add(token);
        _balances[to] = _balances[to].add(token);
        // address (0) 可以理解为空，有无中生有之意。
        emit Transfer(address(0), to, token);
        return true;
    }
}
