from django.conf.urls import url

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^leaf', views.RenderMap.as_view(), name='leaflet'),
    url(r'^createaccount', views.CreateAccount.as_view(), name='createaccount'),
]
