from django.conf.urls import patterns, url

from DRCA import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'curso/$', views.curso, name='curso'),
    url(r'^aluno/(?P<id>[0-9]+)/$', views.aluno),
)