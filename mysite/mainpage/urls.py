from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^index/index2/$', views.index2),
    url(r'^index/temp/index2$', views.index2)
]

