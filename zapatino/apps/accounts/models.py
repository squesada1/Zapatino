from django.db import models
from django.conf import settings

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.user.username   