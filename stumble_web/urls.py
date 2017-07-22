from django.conf.urls import url

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^createaccount/$', views.signup, name='createaccount'),
    url(r'^leaf/$', views.PlacesNearMe.as_view(), name='near_me'),
    url(r'^leaf/user/profile/$', views.UserProfile.as_view(), name='user_profile'),
]
