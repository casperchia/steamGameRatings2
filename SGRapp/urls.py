from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^username/(?P<steamName>\w+)/$', views.results, name='results'),
    url(r'^id/(?P<steamId>[0-9]+)/$', views.results, name='results'),
    url(r'^goto/$', views.goto, name='goto'),
    # url(r'^username/(?P<username>\w+)/$', views.results, name='results'),
]
