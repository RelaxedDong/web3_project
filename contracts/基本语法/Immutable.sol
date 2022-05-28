pragma solidity ^0.8.0;

contract Immutable {
    // immutable 跟constance类似，不过可以在构造函数里面初始化，然后就不能修改了。
    address public immutable MY_ADDRESS;
    uint public immutable MY_UINT;
    constructor (uint _myUint) {
        MY_ADDRESS = msg.sender;
        MY_UINT = _myUint;
    }
}
