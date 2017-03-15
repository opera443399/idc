# coding=utf-8
# ----------------------------------
# @ 2017/3/13
# @ PC
# ----------------------------------

from django.conf.urls import url
from . import views

app_name = 'hosts'
urlpatterns = [
    #################################### /hosts/xxx
    #
    url(r'^$', views.show_index, name='show_index'),
    url(r'^import/vms$', views.import_vms, name='import_vms'),
    url(r'^import/hosts$', views.import_hosts, name='import_hosts'),
    url(r'^list/vms/(?P<bid>[0-9]+)/$', views.list_vms, name='list_vms'),
    url(r'^list/hosts/(?P<bid>[0-9]+)/$', views.list_hosts, name='list_hosts'),
    url(r'^show/about$', views.show_about, name='show_about'),
]
