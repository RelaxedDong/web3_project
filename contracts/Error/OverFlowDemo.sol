pragma solidity ^0.8.0;

contract OverFlowDemo {
    function overflow() public pure returns (uint8){
        uint8 big = 255 + 1;
        return big;
    }
}
