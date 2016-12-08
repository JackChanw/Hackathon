# -*- coding: utf-8 -*-
import logging

class TopicWriter(object):
    '''
    传入kafka数据
    '''

    def __init__(self, queue):
        self.logger = logging.getLogger('domob.lightmoon')
        self.queue = queue

    def write(self, data):
        '''
        load data 数据 这里单独起一个进程，间隔2s发送到kafka一次数据
        '''
        pass

    def load(self):
        data_list = []
        max_num = 0
        while True:
            try:
                r = self.queue.get_nowait()
                data_list.append(r)
            except Excettion, e:
                continue





    def run():
        while True:
            data = self.load()
            self.write(data)
            time.sleep(2)

