from __future__ import unicode_literals

from django.db import models
from django_mysql.models import SizedBinaryField
from django.contrib.auth.models import UserManager

# Create your models here.

class Uploader(models.Model):
    """
    Details of the applicants are stored in DB
    """
    TIMESTAMP_AS_ID = models.CharField(max_length=20)
    EMAIL           = models.CharField(max_length=50)
    PHONE           = models.CharField(max_length=15)
    FILENAME        = models.CharField(max_length=50)
    FILE            = SizedBinaryField(3)
    STATUS          = models.CharField(default='SUBMITTED', max_length=15)
    CLOSEDON        = models.DateTimeField(default=None,blank=True, null=True)
    
    objects = UserManager()
