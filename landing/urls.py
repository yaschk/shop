from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/', views.landing, name='landing'),
    url(r'^info/', views.info, name='info'),
]