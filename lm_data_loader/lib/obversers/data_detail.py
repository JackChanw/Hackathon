# coding: utf-8

class DataInfo(object):
    '''
    将kafka传入的数据转化为类 方便处理
    '''
    def __init__(self):
        self.product_id = 0
        self.user_ip = ''
        self.event_id = 0
        self.event_ip = ''
        self.behavior = ''
        self.eventPrice = 0.0
        self.eventUrl = ''
        self.eventName = ''
        self.ts = 0
