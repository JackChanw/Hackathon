# -*- coding: utf-8 -*-

import logging
from obversers.data_trans import DataTrans
from Queue import Queue
from pykafka import *
import json
from django.conf import settings

class TopicLoader(object):
    '''
    负责将kafka的数据取出
    '''

    def __init__(self, queue):
        self.logger = logging.getLogger('domob.lightmoon.reader')
        self.queue = queue
        self.client = KafkaClient(hosts=settings.KAFKA_HOST)
        self.topic = self.client.topics[settings.KAFKA_TOPIC_RECIVE]
        self.data_trans = DataTrans()

    def fetch_and_process(self):
        '''
        从kafka取出数据并发送到下游处理
        '''
        consumer = self.topic.get_balanced_consumer(consumer_group="group", \
            zookeeper_connect='10.0.0.207:21815', reset_offset_on_start=True)
        # consumer = self.topic.get_simple_consumer()
        for msg in consumer:
            print msg.value
            try :
                json_obj = json.loads(msg.value)
                print json_obj
                self._publish(json_obj)
            except ValueError, ve:
                print ve
                continue

    def _publish(self, data):
        '''
        发布数据，后期如果出现多个topic的情况就注册多个观察者
        '''
        res = self.data_trans.process(data)
        if res:
            self.queue.put(res)
        print self.queue.qsize()

    def run(self):
        # self.logger.info('Topic reader started!')
        self.fetch_and_process()

if __name__=="__main__":
    queue = Queue()
    reader = TopicReader(queue)
    reader.run()
