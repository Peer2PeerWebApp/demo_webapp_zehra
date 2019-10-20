from django.urls import path

from . import views

#provide mapping, list of all urls
urlpatterns = [

    path('', views.home, name = 'home')


]