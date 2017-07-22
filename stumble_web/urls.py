from django.conf.urls import url

from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from stumble_web.views import CreateAccount


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'index.html'}, name='index'),
    url(r'^home', views.RenderMap.as_view(), name='home'),
    url(r'^createaccount', views.CreateAccount.as_view(), name='createaccount'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
