from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import permissions



#api_root
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
    })


class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ListUsers(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    #assign serializer class
    serializer_class = UserSerializer
    #get all users query set
    queryset = User.objects.all()

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #assign serializer class
    serializer_class = UserSerializer
    #get all users query set
    queryset = User.objects.all()
