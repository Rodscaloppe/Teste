from django.shortcuts import render
from DRCA.tables import *
from DRCA.serializers import *
from django_tables2 import RequestConfig

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html', {})

def aluno(request):
    return render(request, 'index.html', {})

def curso(request):
    departament_id = request.GET.get('id')
    cursos = CursoTable(Curso.objects.all().filter(cod_departamento_id=departament_id))
    serializer = CursoSerializer(cursos, many=True)
    RequestConfig(request).configure(cursos)
    return render(request, 'cursos.html', {'table': cursos})

def departamento(request):
    departamentos = DepartamentoTable(Departamento.objects.all())
    RequestConfig(request).configure(departamentos)
    return render(request, 'departamentos.html', {'table': departamentos})

def aluno(request):
    aluno_id = request.GET.get('id')
    alunos = AlunoTable(Aluno.objects.all().filter(cod_curso_id=aluno_id))
    serializer = CursoSerializer(alunos, many=True)
    RequestConfig(request).configure(alunos)
    return render(request, 'alunos.html', {'table': alunos})

def matricula(request):
    aluno = Aluno.objects.get(id=0)
    curso = Curso.objects.get(cod_curso = aluno.cod_curso)

    if curso.tipo_curso == "Graduação":
        matricular = "ECOM1622"

        disciplina = Disciplina.objects.get(cod_disciplina = matricular)
        disciplinasCursadas = Disciplinas_cursadas.objects.get(matricula_aluno_id=aluno.matricula_aluno,cod_disciplina_id=matricular)

        #Iniciando matricula
        if not disciplina.e_oferecida:
            print("A disciplina não está disponível para matrícula (não oferecida)")

        elif not (aluno.creditos_obrigatorios + aluno.creditos_eletivas) >= disciplina.requisito_credito:
            print("A disciplina não está disponível para matrícula (créditos insuficientes)")

        elif disciplinasCursadas is None:
            print("A disciplina não está disponível para matrícula (disciplina cursada)")

        else:
            Disciplinas_cursadas.create(cod_disciplina_id=matricular, matricula_aluno_id=aluno.matricula_aluno)