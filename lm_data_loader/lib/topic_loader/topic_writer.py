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
                if not sum_dic.has_key(r['eventName']:
                    sum_dic[r['eventName']] = [r, 0]
                sum_dic[r['eventName']][-1] += 1
                max_num += 1
                if max_num > settings.MAXSIZE:
                    self.queue.clear()
                    break
            except Excettion, e:
                break
        d = {
            'total' : max_num,
            'events': data_list
        }
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

