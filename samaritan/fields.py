from django.db import models
from django.conf import settings
from samaritan.utils import USER_MODEL_NAME

__all__ = ['UserForeignKey', 'UserOneToOneField', 'UserManyToManyField']

class UserForeignKey(models.ForeignKey):
    def __init__(self, **kwargs):
        super(UserForeignKey, self).__init__(USER_MODEL_NAME, **kwargs)

class UserOneToOneField(models.OneToOneField):
    def __init__(self, **kwargs):
        super(UserOneToOneField, self).__init__(USER_MODEL_NAME, **kwargs)

class UserManyToManyField(models.ManyToManyField):
    def __init__(self, **kwargs):
        super(UserManyToManyField, self).__init__(USER_MODEL_NAME, **kwargs)
