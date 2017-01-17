from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^logo/main/$', views.main),
    url(r'^index/main/result$', views.result)
]
