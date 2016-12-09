# 灵眸 数据协议

## kafka数据录入协议
|信息 |类型| 备注|
|-------|----|------|
|productId|int|产品线id| 
|userIp   |string|用户ip|
|eventId  |int| 事件id |
|eventIp  |string|事件ip |
|behavior| string|触发事件，点击，激活，浏览|
|eventPrice|int 原始价值乘1000000 | 事件价值 |
|eventUrl| string|事件logo地址|
|eventName|string| 事件内容|
|ts |int| 时间戳|


## json数据格式
- 实时数据请求
```
dataObject
{
	productId   : "产品线id",
	productName : "产品线名称",
	behavior    : "触发事件"，
	address     : "城市"，
	eventName   : "浏览等"，
	userCity    : "",
	eventCity   : ""
}

{
	events:[
		dataObject,
	]
	total: 100
}
```
- 汇总数据请求
{
	eventName : "",
	number : 0,
}

>汇总请求存在redis中


|信息 | 备注|
|-------|------|
|key_{product_id}_event_share|事件价值总计|
|key_events|事件总计数量|
