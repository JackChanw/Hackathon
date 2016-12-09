# coding: utf-8

import logging
import redis
import threading

from django.db import close_old_connections
from obversers.data_detail import DataInfo
from obversers.abstract_observer import AbstractObserver
from db.models import AdDetail, OwAdCreative, OwMediaMedia
from iptrans.ip_trans import GeoIp


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
        self.pool = redis.ConnectionPool(**settings.REDIS_CONFIG)
        self.logger = logging.getLogger('domob.lightmoon')
        self.ad_creative = {}
        self.ad_dict = {}
        self.media = {}
        self.num = 0
        self.data_info = DataInfo()
        self.geo_ip = GeoIp()

    def process(self, data):
        self.data_info.uid = data['uid']
        self.data_info.user_ip = data['userIp']
        self.data_info.media_id = data['mediaId']
        self.data_info.cid = data['cid']
        self.data_info.event = data['event']
        self.data_info.product_id = data['productId']
        get_detail = threading.Thread(target=self.get_detail())
        get_detail.start()
        add_detail = threading.Thread(target=self.add_detail())
        add_detail.start()
        data = self.trans(data)

    def add_detail(self):
        redis_cli = redis.Redis(connection_pool=self.pool)
        redis_cli.incr('key_ads')
        redis_cli.sadd('key_cids', self.data_info.cid)
        redis_cli.sadd('key_medias', self.data_info.media_id)
        # 首席
        if product_id == 1:
            if self.ad_creative.has_key(self.data_info.cid):
                user_share = self.ad_creative[self.data_info.cid].price/100000.0
                redis_cli.incrbyfloat('key_user_share', user_share)
        # dvx
        if product_id == 2:
            if self.media.has_key(self.data_info.media_id):
                media_share = self.media[self.data_info.media_id].video_floor_price/1000000.0
                redis_cli.incrbyfloat('key_media_share', media_share)


    def get_detail(self):
        if not self.ad_creative.has_key(self.data_info.cid):
            try:
                ad_creative = OwAdCreative.objects.filter(uid=uid)
                self.ad_creative[uid] = ad_creative
            except Exception, e:
                self.logger.error(e)
        if not self.ad_detail.has_key(uid):
            try:
                ad_detail = AdDetail.objects.filter(uid=uid)
                self.ad_detail = ad_detail
            except Exception, e:
                self.logger.error(e)
        if not self.media.has_key(media_id):
            try:
                self.media[uid] = OwMediaMedia.objects.filter(mid=media_id)
            except Exception, e:
                self.logger.error(e)

    def trans_data(data):
        tmp_data = {}
        tmp_data['productId'] = data['productId']
        if self.ad_creatice.has_key(self.data_info.cid):
            tmp_data['productName'] = self.ad_creative[self.data_info.cid].name
        else:
            return None
        tmp_data['event'] = data['event']
        user_ip_detail = self.geo_ip.find(data['userIp'])
        self.logger.info('Geo get ip country %s', ip_detail.country_name)
        if user_ip_detail.country_name != '中国':
            return None 
        tmp_data['address'] = user_ip_detail.city_name
        tmp_data['userPoint'] = {}
        tmp_data['userPoint']['x'] = user_ip_detail.longitude
        tmp_data['userPoint']['y'] = user_ip_detail.latitude
        ad_ip_detail = self.geo_ip.find(data[])


