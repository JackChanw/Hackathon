# coding: utf-8

import logging
import redis
import threading
import json

from obversers.data_detail import DataInfo
from obversers.abstract_observer import AbstractObserver
from iptrans.ipip import IP
from obversers.constant import city_list
from django.conf import settings


class DataTrans(object):
    '''
    实时数据存入Queue中
    非实时数据存入redis中
    '''

    def __init__(self):
        self.pool = redis.ConnectionPool(**settings.REDIS_CONFIG)
        self.logger = logging.getLogger('domob.lightmoon')
        self.ad_creative = {}
        self.ad_dict = {}
        self.media = {}
        self.num = 0
        self.data_info = DataInfo()
        self.ipfinder = IP() 
        self.ipfinder.load(settings.IPDB)

    def process(self, data):
        self.data_info.product_id = data['productId']
        self.data_info.user_ip    = data['userIp']
        self.data_info.event_id   = data['eventId']
        self.data_info.event_ip   = data['eventIp']
        self.data_info.behavior   = data['behavior']
        self.data_info.eventPrice = data['eventPrice']
        self.data_info.eventUrl   = data['eventUrl']
        self.data_info.eventName  = data['eventName']
        add_detail = threading.Thread(target=self.add_detail)
        add_detail.start()
        return self.trans_data(data)

    def add_detail(self):
        redis_cli = redis.Redis(connection_pool=self.pool)
        redis_cli.incr('key_events')
        key = 'key_%d_event_share'%self.data_info.product_id
        price = self.data_info.eventPrice / 1000000.0
        redis_cli.incrbyfloat(key, price)

    def trans_data(self, data):
        tmp_data = {}
        tmp_data['productId'] = self.data_info.product_id
        tmp_data['userIp']    = self.data_info.user_ip
        tmp_data['eventId']   = self.data_info.event_id   
        tmp_data['behavior']  = self.data_info.behavior   
        tmp_data['eventUrl']  = self.data_info.eventUrl 
        tmp_data['eventName'] = self.data_info.eventName
        user_ip = self.ipfinder.find(self.data_info.user_ip).strip().split('\t')
        user_country = user_ip[0]
        if user_ip[0] == 'N/A' or user_country != '中国':
            return None
        event_ip = self.ipfinder.find(self.data_info.event_ip).strip().split('\t')
        event_country = event_ip[0]
        if event_ip[0] == 'N/A' or event_country != '中国':
            return None
        tmp_data['userCity']  = user_ip[-1]
        tmp_data['eventCity'] = event_ip[-1]
        if not city_list.has_key(tmp_data['userCity'].encode('utf-8'))\
            or not city_list.has_key(tmp_data['eventCity'].encode('utf-8')): 
            return None
        return json.dumps(tmp_data)

