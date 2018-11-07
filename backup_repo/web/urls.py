from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notice/$', views.notice, name='notice'),
    url(r'^notice/(?P<post_id>\d+)$', views.detail, name='detail'),
    url(r'^terms$', views.term, name='term'),
]
