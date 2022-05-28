// SPDX-License-Identifier: MIT
// https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

pragma solidity ^0.8.0;

contract demo {
    mapping(address => uint256) public addressToAmountFunded;
    function fundNow() public payable {
        // msg.sender: sender call
        // msg.value: how much send
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function getVersion() external view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    function getLatestPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        // return tuples
//        (
//            uint80 roundID,
//            int price,
//            uint startedAt,
//            uint timeStamp,
//            uint80 answeredInRound
//        ) = priceFeed.latestRoundData();
//        return uint256(price);
        (
            /*uint80 roundID*/, // 这些值不用返回，也等于(,uint256 price,,,)
            uint256 price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        return price;
    }
}
