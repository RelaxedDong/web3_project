pragma solidity ^0.8.0; // work > 0.8.x < 0.9.0


contract SimpleStorage {
    // uint256 favorateUint = 999; // size of 256 bits or uint 256
    // bool favorateBool = false;
    // string favorateString = "hello world";
    // int256 favorateInt = -1;
    // address favorateAddr = 0x3Fef480B611d0adD76a4255f2aCEccbDb435E519;
    // bytes32 favorateBytes = "cat";

    // 默认是 internal
    // this will initial as 0;
    // 这里类似于view function, 部署后btn颜色跟view\pure function一样！
//    uint256 public favorateUint ;
//    function store(uint256 _favorateNum) public {
//        favorateUint = _favorateNum;
//    }
//
//    // view pure  are non-state changeing functions
//    function getStore() public view returns (uint256) {
//        return favorateUint;
//    }
//
//    // purely do some type of math
//    function pureFunction(uint256 favorateNun) public pure returns (uint256) {
//        return favorateNun+1;
//    }
}