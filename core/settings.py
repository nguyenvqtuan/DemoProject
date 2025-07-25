import os

ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .settings_production import *
elif ENVIRONMENT == 'staging':
    from .settings_staging import *
else:
    from .settings_development import *
