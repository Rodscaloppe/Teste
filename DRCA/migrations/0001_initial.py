# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_aluno', models.CharField(max_length=100)),
                ('matricula_aluno', models.IntegerField()),
                ('creditos_obrigatorios', models.IntegerField()),
                ('creditos_eletivas', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_curso', models.CharField(max_length=100)),
                ('cod_curso', models.CharField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_departamento', models.CharField(max_length=40)),
                ('cod_departamento', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_disciplina', models.CharField(max_length=50)),
                ('cod_disciplina', models.CharField(max_length=7)),
                ('creditos_disciplina', models.IntegerField()),
                ('e_obrigatoria', models.BooleanField(default=False)),
                ('e_oferecida', models.BooleanField(default=False)),
                ('requisito_credito', models.IntegerField()),
                ('cod_curso', models.ForeignKey(to='DRCA.Curso')),
                ('requisito_disciplina', models.ManyToManyField(related_name='requisito_disciplina_rel_+', blank=True, to='DRCA.Disciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplinas_cursadas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cod_disciplina', models.ForeignKey(to='DRCA.Disciplina')),
                ('matricula_aluno', models.ForeignKey(to='DRCA.Aluno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_professor', models.CharField(max_length=100)),
                ('matricula_professor', models.IntegerField()),
                ('cod_departamento', models.ForeignKey(to='DRCA.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='curso',
            name='cod_departamento',
            field=models.ForeignKey(to='DRCA.Departamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='cod_curso',
            field=models.ForeignKey(to='DRCA.Curso'),
            preserve_default=True,
        ),
    ]
