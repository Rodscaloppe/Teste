from django.conf.urls import patterns, url

from DRCA import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'curso/(\d+)/', views.curso, name='curso'),
    url(r'aluno', views.aluno, name='aluno'),
    url(r'aluno/(\d+)/', views.aluno, name='addaluno'),
)