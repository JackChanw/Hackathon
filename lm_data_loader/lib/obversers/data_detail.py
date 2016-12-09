# coding: utf-8

class DataInfo(object):
    '''
    将kafka传入的数据转化为类 方便处理
    '''
    def __init__(self):
        self.uid = 0
        self.user_ip = ''
        self.media_id = 0
        self.cid = 0
        self.event = 0
        self.product_id = 0
