# -*- encoding=utf-8 -*-
from abc import ABCMeta, abstractmethod


class AbstractObserver(object):
    '''
    所有的观察者通过订阅主题来对需要的数据进行处理
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, data):
        pass

    def notify(self, data):
        self.process(data)
