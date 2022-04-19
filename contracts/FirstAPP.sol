pragma solidity ^0.8.0;

contract FirstAPP {
    // default: 0: uint256: 0
    uint public count;
    function get () public view returns (uint) {
        return count;
    }
    function inc() public {
        count += 1;
    }
    function dec() public {
        count -= 1;
    }
}
