# coding: utf-8

import logging
import redis
import threading
import json

from django.db import close_old_connections
from obversers.data_detail import DataInfo
from obversers.abstract_observer import AbstractObserver
from db.models import AdDetail, OwAdCreative, OwMediaMedia
from iptrans.ipip import IP


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
        self.geo_ip = GeoIp()
        self.ipfinder = IP.load(settings.IPDB) 

    def process(self, data):
        data = json.loads(data)
        self.data_info.product_id = data['productId']
        self.data_info.user_ip    = data['userIp']
        self.data_info.event_id   = data['eventId']
        self.data_info.event_ip   = data['eventIp']
        self.data_info.behavior   = data['behavior']
        self.data_info.eventPrice = data['eventPrice']
        self.data_info.eventUrl   = data['eventUrl']
        self.data_info.eventName  = data['eventName']
        add_detail = threading.Thread(target=self.add_detail())
        add_detail.start()
        data = self.trans(data)

    def add_detail(self):
        redis_cli = redis.Redis(connection_pool=self.pool)
        redis_cli.incr('key_events')
        key = 'key_%s_event_share'%self.data_info.product_id
        price = self.data_info.eventPrice / 1000000.0
        redis_cli.incrfloat(key, price)

    def trans_data(data):
        tmp_data = {}
        tmp_data['productId'] = self.data_info.product_id
        tmp_data['userIp']    = self.data_info.user_ip
        tmp_data['eventId']   = self.data_info.event_id   
        tmp_data['behavior']  = self.data_info.behavior   
        tmp_data['eventUrl']  = self.data_info.eventUrl 
        tmp_data['eventName'] = self.data_info.eventName
        user_ip = self.ipfinder.find(self.data_info.user_ip).split(' ')
        user_country = user_ip[0]
        if user_ip[0] == 'N/A' or user_country != '中国':
            return None
        event_ip = self.ipfinder.find(self.data_info.event_ip).split(' ')
        event_country = event_ip[0]
        if event_ip[0] == 'N/A' or event_country != '中国':
            return None
        tmp_data['userCity']  = user_ip[-1]
        tmp_data['eventCity'] = event_country[-1]
        return jons.loads(tmp_data)
