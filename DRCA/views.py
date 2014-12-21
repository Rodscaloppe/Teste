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
    #Gerando a tabela de disciplinas já matriculadas.
    disciplinasCursadas = DisciplinaCursadaTable(Disciplinas_cursadas.objects.all().filter(matricula_aluno_id=aluno_id))

    #iniciando geração de matriculas.
    disciplinasCursadas_id = Disciplinas_cursadas.objects.filter(matricula_aluno_id=aluno_id)

    disciplinas = DisciplinaTable(Disciplina.objects.all().exclude(id__in=disciplinasCursadas_id))

    #django-tables: geração das tabelas
    RequestConfig(request).configure(disciplinasCursadas)
    RequestConfig(request).configure(disciplinas)
    return render(request, 'disciplinas.html', {'table': disciplinasCursadas, 'table2': disciplinas})

def matricula(request):
    aluno_id = request.GET.get('aluno_id')
    disciplina_id = request.GET.get('disciplina_id')

    alunos = Aluno.objects.all().filter(id=aluno_id)
    disciplina_id = Disciplina.objects.all().filter(id=disciplina_id)




