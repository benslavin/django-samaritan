from django.conf import settings
from samaritan import DEFAULT_USER_MODEL

USER_MODEL_NAME = getattr(settings, 'USER_MODEL', DEFAULT_USER_MODEL)
