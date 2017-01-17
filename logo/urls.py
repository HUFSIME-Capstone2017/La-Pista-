from django.conf.urls import url,include
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^logo/$', views.logo),
    url(r'^logo/main/$', views.main),
    url(r'^logo/main/result/$', views.result),
    url(r'^logo/main/index/$', views.index),

]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)