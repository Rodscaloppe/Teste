from django.shortcuts import render
from DRCA.tables import *
from django_tables2 import RequestConfig

def index(request):
    return render(request, 'index.html', {})

def aluno(request):
    return render(request, 'index.html', {})

def curso(request):
    departamento_id = request.GET.get('id')
    cursos = CursoTable(Curso.objects.all().filter(cod_departamento_id=departamento_id))
    RequestConfig(request).configure(cursos)
    return render(request, 'cursos.html', {'table': cursos})

def departamento(request):
    departamentos = DepartamentoTable(Departamento.objects.all())
    RequestConfig(request).configure(departamentos)
    return render(request, 'departamentos.html', {'table': departamentos})

def aluno(request):
    curso_id = request.GET.get('id')
    alunos = AlunoTable(Aluno.objects.all().filter(cod_curso_id=curso_id))
    RequestConfig(request).configure(alunos)
    return render(request, 'alunos.html', {'table': alunos})

def disciplina(request):
    aluno_id = request.GET.get('id')
    disciplinasCursadas = DisciplinaTable(Disciplinas_cursadas.objects.all().filter(matricula_aluno_id=aluno_id))
    disciplinas = DisciplinaTable(Disciplina.objects.all().filter(cod_curso_id=aluno_id))
    RequestConfig(request).configure(disciplinasCursadas)
    RequestConfig(request).configure(disciplinas)
    return render(request, 'disciplinas.html', {'table': disciplinasCursadas, 'table2': disciplinas})

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