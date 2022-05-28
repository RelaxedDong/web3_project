pragma solidity ^0.8.0;

contract memory_storage {
    //状态存储
    uint private _state;
    // 这里会报错>>  Expected identifier but got 'memory'：在 Solidity 中，局部变量若是整型、定长字节数组等类型，就会随着指令的运行入栈、出栈。
    // int32 public memory a;
    // 如果一个局部变量属于变长字节数组、字符串、结构体等类型，其通常会被 memory 修饰符修饰，以表明存储在内存中。

    function set(uint state) public {
        //栈存储, 变量值 1 会被读出，通过 PUSH 操作压入栈顶：
        uint i = 1;
        //内存存储
        string memory str = "aaa";
    }
}
