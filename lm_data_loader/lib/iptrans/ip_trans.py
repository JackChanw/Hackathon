# coding: utf-8

import geoip2.database
from django import settings
from iptrans.ip_detail import IpDetail

class GeoIp(object):

    def __init__(self):
        self.reader = geoip2.database.Reader(settings.IPDB)
        self.logger = logger.getLogger('domob.lightmoon.geoip')

    def find(ip):
        '''
        返回国家，省份，城市信息, 经纬度信息
        '''
        result = self.reader.city(ip) 
        ip_detail = IpDetail()
        try:
            ip_detail.city_name = result.city.name['zh-CN']
            ip_detail.country_name = result.country.name['zh-CN']
            ip_detail.latitude = result.location.latitude
            ip_detail.longitude = result.location.longitude
        except Exception, e:
            self.logger.error(e)

        return ip_detail

