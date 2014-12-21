from rest_framework import serializers
from DRCA.models import *

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome_curso', 'cod_curso', "cod_departamento_id", "tipo_curso")

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nome_departamento', 'cod_departamento')

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('id', 'nome_disciplina', 'cod_disciplina', 'creditos_disciplina', 'e_obrigatoria', 'e_oferecida', 'requisito_credito', 'requisito_disciplina')

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome_aluno', 'matricula_aluno', 'creditos_obrigatorios', 'creditos_eletivas', 'cod_curso_id')