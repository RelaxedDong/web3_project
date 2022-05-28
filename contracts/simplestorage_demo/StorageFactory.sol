// SPDX-License-Identifier: MIT
// https://github.com/PatrickAlphaC/storage_factory/blob/main/SimpleStorage.sol

pragma solidity ^0.8.0; // work > 0.8.x < 0.9.0
import "./SimpleStorage.sol";

// contract StorageFactory {
//     SimpleStorage [] public storageContractList;

//     function createSimpleStorageContract () public {
//         // new SimpleStorage() 初始化一个合约
//         // simplestorage：变量名，类型：SimpleStorage
//         SimpleStorage mysimplestorage = new SimpleStorage();
//         storageContractList.push(mysimplestorage);
//     }

//     function mystore(uint256 _facotoryContractInde, uint256 _favoriteNumber) public {
//         // SimpleStorage mycontract = SimpleStorage(address(storageContractList[_facotoryContractInde]));
//         // mycontract.store(_favoriteNumber);
//         SimpleStorage(address(storageContractList[_facotoryContractInde])).store(_favoriteNumber);
//     }

//     function myretrieve(uint256 _facotoryContractInde) public view returns(uint256){
//         // SimpleStorage mycontract = SimpleStorage(address(storageContractList[_facotoryContractInde]));
//         // return mycontract.retrieve();
//         return SimpleStorage(address(storageContractList[_facotoryContractInde])).retrieve();
//     }

// }


// 继承合约
contract StorageFactory is SimpleStorage {
    

}