import json

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NAVUser
        fields = ('id', 'first_name', 'last_name', 'company_name', 'age','city', 'state','zip', 'email', 'web')
