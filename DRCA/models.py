from django.db import models


class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=40)
    cod_departamento = models.CharField(max_length=3)


class Professor(models.Model):
    nome_professor = models.CharField(max_length=100)
    matricula_professor = models.IntegerField()
    cod_departamento = models.ForeignKey(Departamento)


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    cod_curso = models.CharField(max_length=7)
    cod_departamento = models.ForeignKey(Departamento)
    tipo_curso = models.CharField(max_length=11)


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    matricula_aluno = models.IntegerField()
    creditos_obrigatorios = models.IntegerField()
    creditos_eletivas = models.IntegerField()
    cod_curso = models.ForeignKey(Curso)


class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=50)
    cod_disciplina = models.CharField(max_length=7)
    cod_curso = models.ForeignKey(Curso)
    creditos_disciplina = models.IntegerField()
    e_obrigatoria = models.BooleanField(default=False)
    e_oferecida = models.BooleanField(default=False)
    requisito_credito = models.IntegerField()
    requisito_disciplina = models.ManyToManyField("self", blank=True)


class Disciplinas_cursadas(models.Model):
    matricula_aluno = models.ForeignKey(Aluno)
    cod_disciplina = models.ForeignKey(Disciplina)


