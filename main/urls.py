from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [

    path('', index, name='home'),
]