# 灵眸 数据协议

## kafka数据录入协议
|信息 | 备注|
|-------|------|
|productId|产品线id| 
|userIp   | 用户ip |
|eventId  | 事件id |
|eventIp  | 事件ip |
|behavior| 触发事件，点击，激活，浏览|
|eventPrice| 事件价值|
|eventUrl| 事件logo地址|
|eventName| 事件内容|
|ts | 时间戳|


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
