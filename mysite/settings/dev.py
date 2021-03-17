from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
