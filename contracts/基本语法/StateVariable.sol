pragma solidity ^0.8.0;
    /*
    Solidity中的三种变量:
        local
            函数内申明，不会存储区块链
        state
            函数外申明，存储区块链
        global
            blockchain 的共有信息
    */
contract StateVariable {
    // 变量，会被放到contract自由的storage里面
    // State variables are stored on the blockchain.
    string name;
    address owner; // address->(account、contract address)
    // 主要做初始化
    constructor () {
        name = "unknown";
        owner = msg.sender;
    }
    function SetName(string memory _name) public returns (string memory) {
        // Local variables are not saved to the blockchain.
        uint = 256;
        // 全局变量
        uint timestamp = block.timestamp; // Current block timestamp
        address sender = msg.sender; // address of the caller

        if(msg.sender == owner) {
            // 写与更新需要发起transaction
            name = _name;
        } else {
            revert("Permission Denied!");
        }
        return name;
    }

    function GetName() public view returns (string memory) {
        // 读取state变量，is free，因为不会产生交易
        return name;
    }
}
