import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BROKER_URL = 'redis://10.0.0.206:6395/9'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_ENABLE_UTC=False
CELERY_ACKS_LATE=True
CELERY_DISABLE_RATE_LIMITS=True
CELERY_IGNORE_RESULT=True

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
        'sensor': {
            'format': "%(message)s"
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'celeryHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'when': 'D',
            'interval': 1,
            'filename': os.path.join(BASE_DIR, 'log/daily/celery.log'),
        },
        'sensorHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'sensor',
            'filename': os.path.join(BASE_DIR, 'log/daily/sensor.log'),
            'when': 'D',
            'interval': 1,
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'dbb_robot_ai': {
            'level': 'DEBUG',
            'handlers': ['celeryHandler'],
            'propagate': False,
        },
    },
}
