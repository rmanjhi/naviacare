from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class Users(Document):
#     first_name = fields.StringField(default="")
#     last_name = fields.StringField(default="")
#     company_name = fields.StringField(default="")
#     age = fields.StringField(default="")
#     city = fields.StringField(default="")
#     state = fields.StringField(default="")
#     zip = fields.StringField(default="")
#     email = fields.StringField(default="")
#     web = fields.StringField(default="")
#     updated = fields.DateTimeField()
#     created = fields.DateTimeField(default=dt.now())

class NAVUser(AbstractUser):
    first_name = models.CharField(max_length=255, help_text='Enter first Name.')
    last_name = models.CharField(max_length=255, help_text='Enter Last Name.')
    company_name = models.CharField(max_length=255, help_text='Enter company Name.')
    age = models.IntegerField(default = 25, help_text='Enter age.')
    city = models.CharField(max_length=255, help_text='Enter city.')
    state = models.CharField(max_length=255, help_text='Enter state Name.')
    zip =models.IntegerField(default=122005)
    email = models.CharField(max_length=255, help_text='Enter email Name.')
    web = models.CharField(max_length=255, help_text='Enter web Name.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
