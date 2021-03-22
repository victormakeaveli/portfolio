from .base import *

DEBUG = False

ALLOWED_HOSTS = ['code-eager.herokuapp.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'