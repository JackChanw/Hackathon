# 灵眸 数据协议

## kafka数据录入协议
|信息 | 备注|
|-------|------|
|productId|产品线id| 
|userIp   | 用户ip |
|eventId  | 事件id |
|behavior| 触发事件，点击，激活，浏览|
|eventPrice| 事件价值|
|ts | 时间戳|

## event 事件表
|信息 | 备注|
|-------|------|
|eventId| 事件id|
|name| 事件名称|
|ip| 事件ip地址|
|url| 事件logo|


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
	userPoint   : {
		x     : "经度"，
		y     : "纬度"
	}，
	eventPoint  : {
		x     : "经度"，
		y     : "纬度"
	}
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
|key_media_share|媒体分成总计|
|key_ads|分发广告总计数量|
|key_user_share|用户分成总计|
|key_cids|分发广告创意集合|
|key_media_ids|对接媒体集合|

