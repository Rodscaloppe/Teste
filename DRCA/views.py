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

@api_view(['GET', ])
def curso(request):
    departamento_id = request.GET.get('id')
    #serializer = DisciplineSerializer(disciplines, many=True)
    table = CursoTable(Curso.objects.all().filter(cod_departamento_id=departamento_id))
    RequestConfig(request, paginate={"per_page": 25}).configure(table)
    return render(request, 'cursos.html', {'table': table})

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