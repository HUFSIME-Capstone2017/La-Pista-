"""lapista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from basic import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
import basic
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^main', views.main),
    url(r'^1main', views.westernmain),
    url(r'^2main', views.emain),
    url(r'^mainerror', views.result),
    url(r'^result', views.result),
    url(r'^staytime', views.staytime),
    url(r'^price', views.price),
    url(r'^course', views.course),
    url(r'^explain', views.explain),
    url(r'^final', views.final),
    url(r'^list', views.list),
    url(r'^detail', views.detail),
<<<<<<< HEAD:lapista/urls.py
    url(r'^apiresult', views.apiresult),
    url(r'^research', views.research),
    url(r'^desearch', views.desearch),
    # url(r'^geo', views.tsp),
    url(r'^geo', views.geo),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.signin),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^trend/$', views.trend),
    url(r'^trenderror/$', views.trend),
    url(r'^graph/$', views.graph),
    url(r'^fordb', views.fordb),

=======
    url(r'^deo', views.warehouse),
    url(r'^logo', views.logo),
>>>>>>> 57411476c987063ea112aac01b3144f73def7658:lapista/lapista/urls.py
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
