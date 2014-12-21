from django.test import TestCase
from DRCA.models import *

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

