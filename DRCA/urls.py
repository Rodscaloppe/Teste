from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from DRCA import views

urlpatterns = patterns(
    'DRCA.views',
    url(r'^$', 'index'),

    #api
    url(r'^curso/$', views.curso,
    #url(r'^api/disciplina/$', views.disciplina.as_view()),
    url(r'^aluno/$', views.aluno,
    )))
