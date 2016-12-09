# -*- coding: utf-8 -*-

import logging
import json
from django.conf import settings

class TopicWriter(object):
    '''
    传入kafka数据
    '''

    def __init__(self, queue):
        self.logger = logging.getLogger('domob.lightmoon.writer')
        self.queue = queue

    def write_data(self, data):
        '''
        load data 数据 这里单独起一个进程，
        间隔2s发送到kafka一次数据
        '''
        pass

    def write_sum(self, sum_data):
        pass

    def load(self):
        data_list = []
        sum_dic = {}
        max_num = 0
        while True:
            try:
                r = self.queue.get_nowait()
                data_list.append(r)
                sum_dic[r['adName']] = sum_dic.get(r['adName'], 0) + 1
                max_num += 1
                if max_num > settings.MAXSIZE:
                    self.queue.clear()
                    break
            except Excettion, e:
                continue
        d = {
                'total' : max_num,
                'events': data_list
        }
        return json.dumps(d), json.dumps(sum_data)


    def run():
        self.logging.info('Topic writer started!')
        while True:
            start = time.time()
            data, sum_data = self.load()
            self.write(data)
            self.write_sum(sum_data)
            end = time.time()
            self.logging.info('Topic writer load finish cost %f', start-end)
            time.sleep(2)

