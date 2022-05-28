pragma solidity ^0.8.0;

contract SimpleStorage {
    // pure 完全不存取 state
    function sayHello() public pure returns (string memory){
        return 'hello, world';
    }
}
//public: 大家都可以呼叫，全公开
//external（外部的）: contract外部可以呼叫，内部不可呼叫
//internal（内部的）: contract外部不可以呼叫，内部可呼叫
//private: 只允许被 contract 内呼叫，不能是先呼叫某个func，再去呼叫某个private func
