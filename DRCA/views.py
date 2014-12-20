from django.shortcuts import render
from django_tables2 import RequestConfig
from DRCA.tables import *
from DRCA.models import *


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