# lm_data_loader
用于从kafka中读取数据，整理后再录入到kafka中。
统计数据存入到redis中

## web_rest_api

- 前端通过使用proxy rest api 请求kafka数据，用于展示

## topic_loader 

- topic_loader.topic_loader 读入kafka协议信息
- topic_loader.topic_writer 录入kafka信息
>对于不能完全消耗完的数据,丢弃部分数据，减轻前端负担，提高数据私密性

## iptrans

- 使用ip库，解析为城市信息

## obversers

- 注册观察者，消费读入的kafka数据
