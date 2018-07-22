from django.conf.urls import url

from rsvp import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^info/$', views.Info.as_view(), name='info'),
    url(r'^rsvp/$', views.ResponseCreate.as_view(), name='response-create'),
    url(r'^rsvp/done/$', views.ResponseDone.as_view(), name='response-done'),
    url(r'^registry/$', views.Registry.as_view(), name='registry'),
]
