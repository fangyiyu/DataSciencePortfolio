from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict, name="predict"),
    url(r'^graph/$', views.Graph.as_view(), name='graph'),
]



