pragma solidity ^0.8.0;
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/math/SafeMath.sol";
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/IERC20.sol";

contract my_erc20 is IERC20 {
    using SafeMath for uint256;
        // transferFrom
    event Transfer(address indexed from, address indexed to, uint256 value);

    // approve
    event Approval(address indexed owner, address indexed spender, uint256 value);

    uint256 private _totalSupply;
    mapping(address => uint256) _balances;
    mapping(address => mapping(address => uint256)) _approve;
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // 一个地址持有的token的数量
    // address => uint256
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }
    // msg.sender -> to 转 amount个token，返回bool
    // 会执行 Emits a {Transfer} event.
    function transfer(address to, uint256 amount) external returns (bool) {
         return _transfer(from, to, amount);
    }

    // 获取 owner 授权给 spender 可使用的token数量
    function allowance(address owner, address spender) external view returns (uint256) {
        return _approve[owner][spender];
    }
    // msg.sender -> spender 可使用amount个token
    function approve(address spender, uint256 amount) external returns (bool) {
         _approve[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // 转移token。有个隐藏概念：from_address 授权过给 msg.sender，花的是from_address授权给msg.sender的token.
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        _approve[from][msg.sender] = _approve[from][msg.sender].sub(amount);
        return _transfer(from, to, amount);
    }
    // transferFrom、transfer都有使用，直接封装一下
    function _transfer(address to, uint256 amount) internal returns (bool) {
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[to] = _balances[to].add(amount);
        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
