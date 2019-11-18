import os

# App settings
CDN_A_ADDR = os.getenv('CDN_A_ADDR')
CDN_B_ADDR = os.getenv('CDN_B_ADDR')
CDN_A_WEIGHT = int(os.getenv('CDN_A_WEIGHT', '10'))
CDN_B_WEIGHT = int(os.getenv('CDN_B_WEIGHT', '20'))
ORIGIN_WEIGHT = int(os.getenv('ORIGIN_WEIGHT', '1'))

# Redis settings
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_DATABASE = int(os.getenv('REDIS_DATABASE', '0'))
REDIS_MIN_SIZE_POOL = int(os.getenv('REDIS_MIN_SIZE_POOL', '10'))
REDIS_MAX_SIZE_POOL = int(os.getenv('REDIS_MAX_SIZE_POOL', '100'))

# Logging
ACCESS_LOG = os.getenv('ACCESS_LOG', False)
