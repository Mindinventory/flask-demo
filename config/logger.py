import logging.config

print("Loading default log config.")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'key_value': {
            'format': 'timestamp:%(asctime)s | loglevel:%(levelname)s | module:%(module)s | file:%(filename)s | line:%(lineno)d | %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'key_value',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'gunicorn.error': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'app': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("app")
print("Initialized", logger)