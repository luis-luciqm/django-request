from django.urls import path

from .viewsets import *

urlpatterns = [
    path('register_analytics/', RequestPechinchouSaveViewSet.as_view(), name='register_analytics'),

]