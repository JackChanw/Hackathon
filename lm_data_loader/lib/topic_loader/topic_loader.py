# -*- coding: utf-8 -*-

class TopicReader(object):
    '''
    负责将kafka的数据取出
    '''

    def __init__(self):
        pass

    def fetch_and_process(self):
        '''
        从kafka取出数据并发送到下游处理
        '''

    def _publish(self, data):
        '''
        发布数据，后期如果出现多个topic的情况就注册多个观察者
        '''



