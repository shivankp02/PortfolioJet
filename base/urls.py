from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contact', views.contact, name='contact'),
    path('enhance', views.enhance, name='enhance'),
    path('template', views.template, name='template'),
    path('Resume', views.details, name='details'),
]