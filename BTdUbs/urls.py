from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^order/(?P<buyer>\w*$)', views.order, name='order'),
    url(r'^selection/$', views.selection, name='selection'),
    url(r'^$', views.welcome, name='welcome'),
]
