from django.conf import settings
from django.db import models
from samaritan.utils import USER_MODEL_NAME

def get_user_model():
    from django.db import models
    APP_NAME, MODEL_NAME = USER_MODEL_NAME.split('.')
    return models.get_model(APP_NAME, MODEL_NAME)

def monkey_patch_my_django():
    from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
    from django.contrib.auth.models import User as DjangoUser
        
    def new_init(self, to, *args, **kwargs):
        if to in ['auth.User', DjangoUser]:
            to = USER_MODEL_NAME
        self.__original__init__(to, *args, **kwargs)
    
    # Avert yer eyes!
    for field in [ForeignKey, ManyToManyField, OneToOneField]:
        field.__original__init__ = field.__init__
        field.__init__ = new_init

if getattr(settings, 'ENABLE_MONKEY_PATCHING_OF_USER_RELATIONSHIPS_EVEN_THOUGH_THIS_IS_A_TERRIBLE_IDEA', False):
    monkey_patch_my_django()
