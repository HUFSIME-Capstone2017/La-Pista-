from django.conf.urls.static import static
from django.conf.urls import url,include
from.import views
from django.conf import settings

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^index/temp/$', views.temp)
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)