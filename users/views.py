from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from datetime import datetime
import jwt
from .serializers import *
from .models import NAVUser as Users
from datetime import datetime
from .helpers import *


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


@api_view(['POST'])
# @permission_classes([AllowAny, ])
def users_operations(request):
    err, msg = requirements(request.data, 'users')
    print(msg)
    if err:
        return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    company = request.data.get('company_name', None)
    age = request.data.get('age', None)
    city = request.data.get('city', None)
    state = request.data.get('state', None)
    zip = request.data.get('zip', None)
    email = request.data.get('email', None)
    web = request.data.get('web', None)
    username = first_name + last_name
    data_dict = {'username': username, 'first_name': first_name, 'last_name': last_name, 'company_name': company,
                 'age': age, 'city': city,
                 'state': state, 'zip': zip, 'email': email, 'web': web}
    print(data_dict)
    users_qs = Users.objects.filter(first_name=first_name)
    if users_qs:
        return Response({"message": "User is already exist"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            Users.objects.create(**data_dict)
            return Response({"message": "User has been created successfully."}, status=status.HTTP_201_CREATED)
        except Exception:
            raise APIException({"message": "Error occur while creating"})


@api_view(['PUT', 'DELETE', 'GET'])
# @permission_classes([AllowAny, ])
def users_modification(request, pk):
    if request.method == 'GET':

        try:
            Users.objects.get(id=pk)
        except Exception:
            raise Exception({"message": "requested User doesn't exist.."})
        users_qs = Users.objects.filter(id=pk)
        if users_qs.exists():
            profile = UserSerializer(users_qs[0]).data
            return Response(profile, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error occurred while fetching the data"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user_id_qs = Users.objects.get(id=pk)
        except Users.DoesNotExist:
            raise APIException({"message": "requested user doesn't exist.."})
        if user_id_qs:
            user_id_qs.delete()
            return Response({"message": "User has been Deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error occurred while deleting the users."}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        err, msg = requirements(request.data, 'users')
        print(msg)
        if err:
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        company = request.data.get('company_name', None)
        age = request.data.get('age', None)
        city = request.data.get('city', None)
        state = request.data.get('state', None)
        zip = request.data.get('zip', None)
        email = request.data.get('email', None)
        web = request.data.get('web', None)
        username = first_name + last_name
        data_dict = {'username': username, 'first_name': first_name, 'last_name': last_name, 'company_name': company,
                     'age': age, 'city': city, 'state': state, 'zip': zip, 'email': email, 'web': web}
        try:
            user_id_qs = Users.objects.get(id=pk)
        except Users.DoesNotExist:
            raise APIException({"message": "requested user doesn't exist.."})
        update_dict = {'first_name': first_name, 'last_name': last_name, 'company_name': company, 'age': age,
                       'city': city,
                       'state': state, 'zip': zip, 'email': email, 'web': web}
        if user_id_qs:
            user_data_qs = Users.objects.filter(id=pk)
            user_data_qs.update(**update_dict)
            return Response({"message": "User has been updated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Error occurred while updating the users."}, status=status.HTTP_400_BAD_REQUEST)
