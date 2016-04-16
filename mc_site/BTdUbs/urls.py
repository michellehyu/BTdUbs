from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^selection/', views.selection, name='selection'),
    url(r'^$', views.welcome, name='welcome'),
]
