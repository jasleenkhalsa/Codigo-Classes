from django.urls import path, include
from appdev.views import home 

urlpatterns = [
    path("", home, name='home')
]