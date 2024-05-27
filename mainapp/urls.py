from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('news', news),
    path('photo', photo),
    path('test', test)
]
