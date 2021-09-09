from .base import *

ALLOWED_HOSTS = ['https://serene-swanson-fbc203.netlify.app/']

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

django_heroku.settings(locals())