pragma solidity ^0.8.0;

contract Mapping {
    //  mapping(keyType => valueType)

    //  KeyType: bytes, string, or any contract
    //  valueType can be any type including another mapping or an array.
    mapping(address => uint) public Balance;
    function get(address addr) public view returns(uint) {
        return Balance[addr];
    }
    function set(address addr, uint _balance) public returns (bool) {
        Balance[addr] = _balance;
        return true;
    }
    function remove(address addr) public {
        delete Balance[addr];
    }
}
