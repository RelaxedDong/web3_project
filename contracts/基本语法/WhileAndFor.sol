pragma solidity ^0.8.0;

contract WhileAndFor {
    /*
    Solidity supports for, while, and do while loops.
    编写无界循环，因为这可能会达到 gas 限制，从而导致您的交易失败。while and do while loops are rarely used.
    */
    function loop () public {
        for(uint i =0;i<10;i++) {
            if (i == 3) {
                continue;
            }
            if (i == 5) {
                break;
            }
        }
        uint j;
        // while loop
        while (j < 10) {
            j++;
        }
    }
}
