# Hackathon

## Light Moon 灵眸

灵眸是一款数据可视化平台，用于将event事件基于ip地址展示。


## Qucik Start

Use Confluent-Platform to setup yor data environment.

How to :
[Confluent-Kafka-Rest-Proxy](http://docs.confluent.io/3.1.1/kafka-rest/docs/index.html)

Get LightMoon :

```
git clone https://github.com/JackChanw/Hackathon.git
```

Setup to you local environment :

```
cd Hackathon/lm_data_loader;
vim conf/settings.py ## kafaka-rest port & var topics

```

Start:

```
python ./lib/lm_data_loader.py

```



### Dependency

- [kafka 0.10.1](http://kafka.apache.org/)
- [zookeeper 3.1.13](http://zookeeper.apache.org/)
- [confluent-kafka-rest-proxy](https://www.confluent.io/)
- [webds](http://webd.is/)
- [echart](http://echarts.baidu.com/)
- [django(orm&settings)](https://www.djangoproject.com/)



### Interface Protocol

[数据录入协议地址](https://github.com/JackChanw/Hackathon/blob/master/NeedAndDesign/v0.2/dataProtocol.md)


## 技术架构

![架构图](NeedAndDesign/LightMoon.jpg)


