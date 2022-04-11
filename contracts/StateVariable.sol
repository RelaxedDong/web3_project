pragma solidity ^0.8.0;

contract StateVariable {
    // 变量，会被放到contract自由的storage里面
    string name;
    address owner; // address->(account、contract address)
    // 主要做初始化
    constructor () {
        name = "unknown";
        owner = msg.sender;
    }
    function SetName(string memory _name) public returns (string memory) {
        if(msg.sender == owner) {
            name = _name;
        } else {
            revert("Permission Denied!");
        }
        return name;
    }

    function GetName() public view returns (string memory) {
        return name;
    }
}
