from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import AbstractUser

# # Create your models here.

class NAVUser(AbstractUser):
    first_name = models.CharField(max_length=255, help_text='Enter first Name.')
    last_name = models.CharField(max_length=255, help_text='Enter Last Name.')
    company_name = models.CharField(max_length=255, help_text='Enter company Name.')
    age = models.IntegerField(default = 25)
    city = models.CharField(max_length=255, help_text='Enter city.')
    state = models.CharField(max_length=255, help_text='Enter state Name.')
    zip =models.IntegerField(default=122005)
    email = models.CharField(max_length=255, help_text='Enter email Name.')
    web = models.CharField(max_length=255, help_text='Enter web Name.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def name(self):
        return self.first_name + self.last_name
