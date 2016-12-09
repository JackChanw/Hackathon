# -*- coding: utf-8 -*-

import logging
import json
import time
from Queue import Queue
from pykafka import *
from django.conf import settings

class TopicWriter(object):
    '''
    传入kafka数据
    '''

    def __init__(self, queue):
        self.logger = logging.getLogger('domob.lightmoon.writer')
        self.queue = queue
        self.client = KafkaClient(hosts=settings.KAFKA_HOST)
        self.topic = self.client.topics[settings.KAFKA_TOPIC_DATA]
        self.producer = self.topic.get_sync_producer()
        self.sum_topic = self.client.topics[settings.KAFKA_TOPIC_SUM_DATA]
        self.sum_producer = self.sum_topic.get_sync_producer()
        self.message_topic = self.client.topics[settings.KAFKA_TOPIC_MESSAGE_DATA]
        self.message_topic = self.client.topics[settings.KAFKA_TOPIC_MESSAGE_DATA]
        self.message_producer = self.message_topic.get_sync_producer()
        self.color_switcher = {
            0: 90,
            1: 20,
            2: 40,
            3: 100
        }

    def write_data(self, data):
        '''
        load data 数据 这里单独起一个进程，
        间隔2s发送到kafka一次数据
        '''
        # with self.topic.get_sync_producer() as producer:
        self.producer.produce(data)
        print "produce one data"

    def write_sum(self, sum_data):
        self.sum_producer.produce(sum_data)
        print "produce one sum_data"

    def write_message(self, message):
        self.message_producer.produce(message)
        
    def load(self):
        message_list = []
        data_list = []
        sum_dic = {}
        max_num = 0
        while True:
            try:
                r = self.queue.get_nowait()
                r = json.loads(r)
                data_list.append([
                    {'name': r['userCity']},{'name': r['eventCity'], 'value': self.color_switcher.get(r['productId'])}
                ])
                if len(message_list) < settings.MESSAGE_NUM:
                    message = '''{}用户{}了{}'''.format(
                        r['userCity'], r['behavior'], r['eventName']
                    )
                    message_list.append(message)
                if not sum_dic.has_key(r['eventName']):
                    sum_dic[r['eventName']] = [r, 0]
                sum_dic[r['eventName']][-1] += 1
                max_num += 1
                if max_num > settings.MAXSIZE:
                    self.queue.queue.clear()
                    break
            except Exception, e:
                print e
                break
        sum_data = {
            'eventName': "",
            'eventurl': "",
            'number': 0
        }
        for name, r in sum_dic.items():
            if sum_data['number'] < r[-1]:
                sum_data['eventName'] = name
                sum_data['number'] = r[-1]
                sum_data['eventUrl'] = r[0]
        return json.dumps(data_list), json.dumps(sum_data), json.dumps(message_list)


    def run(self):
        self.logger.info('Topic writer started!')
        while True:
            start = time.time()
            data, sum_data, message = self.load()
            self.write_data(data)
            self.write_sum(sum_data)
            self.write_message(message)
            end = time.time()
            self.logger.info('Topic writer load finish cost %f', start-end)
        #    time.sleep(settings.TIME)
