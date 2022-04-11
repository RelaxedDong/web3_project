pragma solidity ^0.8.0;
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/utils/math/SafeMath.sol";
import "OpenZeppelin/openzeppelin-contracts@4.5.0/contracts/token/ERC20/IERC20.sol";

contract my_erc20 is IERC20 {
    using SafeMath for uint256;

    uint256 private _totalSupply;
    mapping(address => uint256) _balances;
    mapping(address => mapping(address => uint256)) _approve;

    //函数返回代币的名称 - 如 "MyToken" 或 "我的代币"
    function name() public view returns (string) {
        return "hah token";
    }
    // 函数返回代币的代号(通常为字母缩写)，如 "HIX"，"UPT"。
    function symbol() public view returns (string) {
        return "HHT";
    }
    // 返回令牌使用的小数位数 - 例如"8"，意味着将令牌量除以"100000000"以获取其用户表示形式。
    function decimals() public view returns (uint8) {
        return 18;
    }

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
         return _transfer(msg.sender, to, amount);
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
    function _transfer(address from, address to, uint256 amount) internal returns (bool) {
        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);
        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
