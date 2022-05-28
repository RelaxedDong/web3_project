pragma solidity ^0.8.0;

contract Struct {
    uint256 public favoriteNumber1;
    uint256 public favoriteNumber2;
    struct People {
        string name;
        uint256 favoriteNumber;
    }
    People public person = People({favoriteNumber: 666, name: "donghao"});
}
