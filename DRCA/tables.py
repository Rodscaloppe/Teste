import django_tables2 as tables
from django_tables2.utils import A
from DRCA.models import *
from DRCA.views import *


class CursoTable(tables.Table):
    nome_curso = tables.TemplateColumn('<a href="/drca/aluno/?id={{record.id}}">'
                                       '{% load templatetags%}'
                                       '{{record.id|get_nome_curso}}'
                                       '</a>')
    class Meta:
        model = Curso
        attrs = {"class": "paleblue"}


class DepartamentoTable(tables.Table):
    nome_departamento = tables.TemplateColumn('<a href="/drca/curso/?id={{record.id}}">'
                                       '{% load templatetags%}'
                                       '{{record.id|get_nome_departamento}}'
                                       '</a>')
    class Meta:
        model = Departamento
        attrs = {"class": "paleblue"}

class AlunoTable(tables.Table):
    nome_aluno = tables.TemplateColumn('<a href="/drca/disciplina/?id={{record.id}}">'
                                       '{% load templatetags%}'
                                       '{{record.id|get_nome_aluno}}'
                                       '</a>')
    class Meta:
        model = Aluno
        attrs = {"class": "paleblue"}

class DisciplinaTable(tables.Table):
    nome_disciplina = tables.TemplateColumn('<a href="/drca/matricula/?id={{record.id}}">'
                                       '{% load templatetags%}'
                                       '{{record.id|get_nome_disciplina}}'
                                       '</a>')

    class Meta:
        model = Disciplina
        attrs = {"class": "paleblue"}

class DisciplinaCursadaTable(tables.Table):
    nome_disciplina = tables.TemplateColumn(
                                       '{% load templatetags%}'
                                       '{{record.id|get_nome_disciplina}}'
                                       )
    cod_disciplina = tables.TemplateColumn(
                                       '{% load templatetags%}'
                                       '{{record.id|get_cod_disciplina}}'
                                       )
    class Meta:
        model = Disciplinas_cursadas
        attrs = {"class": "paleblue"}
        fields = ('nome_disciplina','cod_disciplina')

