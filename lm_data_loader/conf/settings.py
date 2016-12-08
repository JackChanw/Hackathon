# -*- encoding=utf-8 -*-
"""
Django settings for dbb_sensorsend project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8w%ue9^nq9e+4(pibr#!jyk2r%9mat1_*b5vj5!vomxbjkx#a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# # Database
# # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'searchad',
        'USER': 'domob',
        'PASSWORD': 'domob',
        'HOST': '10.0.0.209',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'




# ip db 存放位置
IPDB = 'conf/GeoLite2-City.mmdb' 

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(thread)d - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'RFHC': {
            'level': 'DEBUG',
            # 定时任务设置按时间切割可能出现漏切的情况，找起来反而比较麻烦
            # 这里按照文件大小进行切割
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'log/lm_common.log'),
            # 200M一个文件进行切割
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 10,
        },
        'RFH': {
            'level': 'DEBUG',
            # 定时任务设置按时间切割可能出现漏切的情况，找起来反而比较麻烦
            # 这里按照文件大小进行切割
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'log/lm.log'),
            # 200M一个文件进行切割
            'maxBytes': 1024 * 1024 * 200,
            'backupCount': 10,
        },
    },
    'loggers': {
        'domob.lightmoon': {
            'level': 'DEBUG',
            'handlers': ['RFH'],
            #'handlers': ['console'],
            'propagate': False
        },
        'domob.lightmoon.common': {
            'level': 'DEBUG',
            'handlers': ['RFHC'],
            #'handlers': ['console'],
            'propagate': False
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    },
}
