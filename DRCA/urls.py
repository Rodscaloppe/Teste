from django.conf.urls import patterns, url
from DRCA import views

urlpatterns = patterns(
    'DRCA.views',
    url(r'^$', 'index'),

    #api
    url(r'^curso/$', views.curso),
    url(r'^departamento/$', views.departamento),
    url(r'^disciplina/$', views.disciplina),
    url(r'^aluno/$', views.aluno,

    ))
