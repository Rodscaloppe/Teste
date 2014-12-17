import django_tables2 as tables
from django.core.urlresolvers import reverse
from django_tables2.utils import A
from DRCA.models import *


class CursoTable(tables.Table):
    nome_curso = tables.LinkColumn('aluno', args=reverse('DRCA.views.aluno', args=(id,)))
    class Meta:
        model = Curso
        attrs = {"class": "paleblue"}


class AlunoTable(tables.Table):
    nome_aluno = tables.LinkColumn('aluno', args=[A('pk')])
    class Meta:
        model = Aluno
        attrs = {"class": "paleblue"}