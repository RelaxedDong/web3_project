pragma solidity ^0.8.0;

contract Pausable {
    bool private _paused;
    event Pause (address addr);
    event UnPause (address addr);
    constructor() public {
        _paused = false;
    }
    modifier whenPaused () {
        require(_paused);
        _;
    }
    modifier whenNotPaused () {
        require(!_paused);
        _;
    }

    function transfer() public whenNotPaused returns (bool) {
        //...
        return true;
    }

    function pause() public whenNotPaused returns (bool) {
        _paused = true;
        emit Pause(msg.sender);
        return true;
    }

    function unpause() public whenNotPaused returns (bool) {
        _paused = false;
        emit UnPause(msg.sender);
        return true;
    }

}
