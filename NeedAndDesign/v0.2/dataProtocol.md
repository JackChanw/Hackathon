# 灵眸 数据协议

## kafka数据录入协议
|信息 | 备注|
|-------|------|
|productId|产品线id| 
|userIp   | 用户ip |
|mediaId  | 媒体id |
|cid | 广告创意id|
|event| 触发事件，1：点击， 2：激活， 3:浏览|
|ts | 时间戳|

## json数据格式
- 实时数据请求
```
dataObject
{
	productId  : "产品线id",
	productName: "产品线名称",
	event      : "触发事件"，
	address    : "城市"，
	adName     : "浏览等"，
	userPoint  : {
		x    : "经度"，
		y    : "纬度"
	}，
	adPoint    : {
		x    : "经度"，
		y    : "纬度"
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

>汇总请求存在redis中


|信息 | 备注|
|-------|------|
|key_media_share|媒体分成总计|
|key_ads|分发广告主总计数量|
|key_user_share|用户分成总计|
|key_acts|激活广告总计|

