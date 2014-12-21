from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from DRCA import views

urlpatterns = patterns(
    'DRCA.views',
    url(r'^$', 'index'),

    #api
    url(r'^curso/$', views.curso),
    url(r'^departamento/$', views.departamento),
    #url(r'^api/disciplina/$', views.disciplina.as_view()),
    url(r'^aluno/$', views.aluno,

    #url(r'^api/disciplines/departament/$', 'list_by_departament', name='list_by_departament'),
    #url(r'edit-offer/(?P<id>\d+)/$', 'DisciplineList.list_by_departament', name='list_by_departament'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ))
