from .settings_development import *
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ['*']  # Update to your domain after first deploy

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'replace-this-with-a-secure-production-key')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Whitenoise static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 