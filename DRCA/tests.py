from django.test import TestCase
from DRCA.models import *
from DRCA.views import *
from django.http import HttpRequest


#Teste dos Models: Aluno, Curso, Departamento e Disciplina, nesta ordem.
class AlunoTestCase(TestCase):
    def setUp(self):
        Aluno.objects.create(id=10, nome_aluno="Jailson", matricula_aluno=2469, creditos_obrigatorios=0,creditos_eletivas=0, cod_curso_id=0)
        Aluno.objects.create(id=11, nome_aluno="Guina", matricula_aluno=425414, creditos_obrigatorios=0,creditos_eletivas=0, cod_curso_id=1)

    def test_nome_Aluno(self):
        nome1 = Aluno.objects.get(nome_aluno="Jailson")
        nome2 = Aluno.objects.get(id=11)
        self.assertEqual(nome1.nome_aluno, 'Jailson')
        self.assertEqual(nome2.nome_aluno, 'Guina')
    def test_curso_Aluno(self):
        curso1 = Aluno.objects.get(nome_aluno="Jailson")
        curso2 = Aluno.objects.get(id=11)
        self.assertEqual(curso1.cod_curso_id, 0)
        self.assertEqual(curso2.cod_curso_id, 1)
    def test_matricula_Aluno(self):
        matricula1 = Aluno.objects.get(nome_aluno="Jailson")
        matricula2 = Aluno.objects.get(id=11)
        self.assertEqual(type(matricula1.matricula_aluno), int)
        self.assertEqual(type(matricula2.matricula_aluno), int)


class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(id=10, nome_curso="Arquitetura", cod_curso='ARQ', cod_departamento_id=10, tipo_curso='Graduação')
        Curso.objects.create(id=11, nome_curso="Design", cod_curso='DSN', cod_departamento_id=10, tipo_curso='Graduação')

    def test_nome_Curso(self):
        nome1 = Curso.objects.get(nome_curso="Arquitetura")
        nome2 = Curso.objects.get(id=11)
        self.assertEqual(nome1.nome_curso, 'Arquitetura')
        self.assertEqual(nome2.nome_curso, 'Design')
    def test_departamento_Curso(self):
        curso1 = Curso.objects.get(nome_curso="Arquitetura")
        curso2 = Curso.objects.get(id=11)
        self.assertEqual(curso1.cod_departamento_id, 10)
        self.assertEqual(curso2.cod_departamento_id, 10)


class DepartamentoTestCase(TestCase):
    def setUp(self):
        Departamento.objects.create(id=10, nome_departamento="Faculdade de Arquitetura", cod_departamento='FAU')
        Departamento.objects.create(id=11, nome_departamento="Faculdade de Direito", cod_departamento='FDA')

    def test_nome_Departamento(self):
        nome1 = Departamento.objects.get(nome_departamento="Faculdade de Arquitetura")
        nome2 = Departamento.objects.get(id=11)
        self.assertEqual(nome1.nome_departamento, 'Faculdade de Arquitetura')
        self.assertEqual(nome2.nome_departamento, 'Faculdade de Direito')
    def test_departamento_Departamento(self):
        departamento1 = Departamento.objects.get(nome_departamento="Faculdade de Arquitetura")
        departamento2 = Departamento.objects.get(id=11)
        self.assertEqual(departamento1.cod_departamento, 'FAU')
        self.assertEqual(departamento2.cod_departamento, 'FDA')


class DisciplinaTestCase(TestCase):
    def setUp(self):
        Disciplina.objects.create(id=10, nome_disciplina="Português", cod_disciplina='PORT', creditos_disciplina=40, e_obrigatoria=0, e_oferecida=1, requisito_credito=10, cod_curso_id=0)
        Disciplina.objects.create(id=11, nome_disciplina="Matemática", cod_disciplina='MAT', creditos_disciplina=60, e_obrigatoria=0, e_oferecida=1, requisito_credito=10, cod_curso_id=0)

    def test_nome_Disciplina(self):
        nome1 = Disciplina.objects.get(nome_disciplina="Português")
        nome2 = Disciplina.objects.get(id=11)
        self.assertEqual(nome1.nome_disciplina, 'Português')
        self.assertEqual(nome2.nome_disciplina, 'Matemática')
    def test_disciplina_Disciplina(self):
        disciplina1 = Disciplina.objects.get(nome_disciplina="Português")
        disciplina2 = Disciplina.objects.get(id=11)
        self.assertEqual(disciplina1.cod_disciplina, 'PORT')
        self.assertEqual(disciplina2.cod_disciplina, 'MAT')
    def test_e_obrigatoria_Disciplina(self):
        disciplina1 = Disciplina.objects.get(nome_disciplina="Português")
        disciplina2 = Disciplina.objects.get(id=11)
        self.assertEqual(type(disciplina1.e_obrigatoria), bool)
        self.assertEqual(type(disciplina2.e_obrigatoria), bool)


#Testando as views se são carregadas corretamente.

class ViewsTest(TestCase):

    def test_index(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<!doctype html>'))
        self.assertTrue(response.content.endswith(b'</html>'))