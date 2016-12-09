# -*- coding: utf-8 -*-
import logging
from obversers.data_trans import DataTrans

class TopicReader(object):
    '''
    负责将kafka的数据取出
    '''

    def __init__(self, queue):
        self.logger = loggint.getLogger('domob.lightmoon.reader')
        self.queue = queue
        self.data_trans = DataTrans()

    def fetch_and_process(self):
        '''
        从kafka取出数据并发送到下游处理
        '''
        pass

    def _publish(self, data):
        '''
        发布数据，后期如果出现多个topic的情况就注册多个观察者
        '''
        res = self.data_trans.process(data)
        if res:
            self.queue.put(res)

    def run():
        self.logger.info('Topic reader started!')
        while True:
            self.fetch_and_process()

