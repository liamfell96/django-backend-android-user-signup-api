from django.urls import include, path
from rest_framework import routers
from . import views

#create router to handle requests to api endpoints

urlpatterns = [
path('api', views.api_root, name = "api-root"),
path('api/users',views.ListUsers.as_view(),name ='user-list'),
path('api/users/<int:pk>', views.UserDetails.as_view(), name = 'user-details')
]
