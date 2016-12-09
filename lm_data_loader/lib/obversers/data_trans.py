# coding: utf-8

import logging
from abstract_observer import AbstractObserver
from django.db import close_old_connections
from db.models import AdDetail, OwAdCreative, OwMediaMedia

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
        self.ad_dict = {}
        self.media_dict = {}
        self.num = 0

    def process(self, data):
        self.num+=1
        uid = data['uid']
        user_ip = data['userIp']
        media_id = data['mediaId']
        cid = data['cid']
        event = data['event']
        product_id = data['product_id']
        ad_creative = OwAdCreative.objects.get(uid=uid)

        #redis
        return data


