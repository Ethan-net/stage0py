from django.urls import path
from .views import *

urlpatterns = [
    path('get/', Get_info)
]
