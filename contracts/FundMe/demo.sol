// SPDX-License-Identifier: MIT
// https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol
// https://github.com/PatrickAlphaC/fund_me/blob/main/FundMe.sol
pragma solidity >= 0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract demo {
    using SafeMathChainlink for uint256;
    address public owner;

    // the first person to deploy the contract is
    // the owner
    constructor() public {
        owner = msg.sender;
    }
    address[] public funders;
    mapping(address => uint256) public addressToAmountFunded;
    function fundNow() public payable {
        // $50
        uint256 minimumUSD = 50 * 10 ** 18;
        require(getConvertRate(msg.value) >= minimumUSD);
//        if (msg.value < minimumUSD) {
//            revert()
//        }

        // msg.sender: sender call
        // msg.value: how much send
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
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
            int price,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();
        // 这里转换成Wei
        return uint256(price * 10000000000);
    }

    function getConvertRate(uint256 _amount)  public view returns(uint256) {
        // 1790580000000000000000
        // return getLatestPrice() * _amount;
        uint256 ehtAmountInUSD = (getLatestPrice() * _amount) / 1000000000000000000;
        return ehtAmountInUSD;
        // 1790

    }
    //modifier: https://medium.com/coinmonks/solidity-tutorial-all-about-modifiers-a86cf81c14cb
    modifier onlyOwner {
    	//is the message sender owner of the contract?
        require(msg.sender == owner, "you not the owner!");
        _; // 代表执行函数
    }

    // onlyOwner modifer will first check the condition inside it
    // and
    // if true, withdraw function will be executed
    function withdraw() payable onlyOwner public {

    	// If you are using version eight (v0.8) of chainlink aggregator interface,
	    // you will need to change the code below to
	    // payable(msg.sender).transfer(address(this).balance);

        msg.sender.transfer(address(this).balance);


        //iterate through all the mappings and make them 0
        //since all the deposited amount has been withdrawn
        for (uint256 index=0; index<funders.length; index++){
            address funder = funders[index];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}
