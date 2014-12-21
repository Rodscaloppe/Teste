from django import template
from DRCA.models import *

register = template.Library()

@register.filter(name='get_nome_departamento')
def get_nome_departamento(value):
    departamento = Departamento.objects.get(id=value)
    return departamento.nome_departamento

@register.filter(name='get_nome_curso')
def get_nome_curso(value):
    curso = Curso.objects.get(id=value)
    return curso.nome_curso

@register.filter(name='get_nome_aluno')
def get_nome_aluno(value):
    aluno = Aluno.objects.get(id=value)
    return aluno.nome_aluno

@register.filter(name='get_nome_disciplina')
def get_nome_disciplina(value):
    disciplina = Disciplina.objects.get(id=value)
    return disciplina.nome_disciplina

@register.filter(name='get_cod_disciplina')
def get_cod_disciplina(value):
    disciplina = Disciplina.objects.get(id=value)
    return disciplina.cod_disciplina