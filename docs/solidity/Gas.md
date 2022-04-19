# Gas
一次交易需要支付：`gas spent * gas price的金额ether`
- gas 是一个计算单位
- gas spent gas 是交易使用的总金额
- gas price ether 是你愿意支付多少gas（每个单位的gas需要支付多少）

> 具有较高gas价格的交易具有更高的优先级被包含在一个块中。 未用完的gas将被退还。

# Gas Limit
花费gas的时候两个上限：
- gas limit（愿意为交易使用的最大gas，自己设置）
- block gas limit（区块中允许的最大gas，由网络设置）
