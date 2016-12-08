# -*- coding: utf-8 -*-

class TopicWriter(object):
    '''
    传入kafka数据
    '''

    def __init__(self):
        pass

    def load(self, data):
        '''
        load data 数据 这里单独起一个进程，间隔5s发送到kafka一次数据
        '''
