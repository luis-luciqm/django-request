from django.urls import path

from .viewsets import *

urlpatterns = [
    # Product
    path('register_analytics/', RequestPechinchouSaveViewSet.as_view(), name='cadastrar_produto'),

]