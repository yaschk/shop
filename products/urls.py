from django.conf.urls import url
from . import views
from products import views
urlpatterns = [
    url(r'^(?P<product_id>\w+)/$', views.product, name='product'),
]