from django.shortcuts import render
from django_tables2 import RequestConfig
from DRCA.tables import *


def index(request):
    return render(request, 'index.html', {})


def curso(request):
    table = CursoTable(Curso.objects.all())
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'cursos.html', {'table': table})


def aluno(request, aluno_id):
    id = request.GET.get('id')
    table = AlunoTable(Aluno.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'alunos.html', {'table': table})