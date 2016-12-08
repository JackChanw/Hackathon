import logging
from abstract_observer import AbstractObserver

class DataTrans(object):
    '''
    转化广告主数据
    转化媒体数据
    转化用户数据
    相关数据累计
    实时数据存入Queue中
    非实时数据存入redis中
    '''

    def __init__(self):
        self.logger = logging.getLogger('domob.lightmoon')

    def process(self, data):
        return data



