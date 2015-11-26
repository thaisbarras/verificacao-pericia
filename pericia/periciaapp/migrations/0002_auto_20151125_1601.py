# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periciaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificacaocadmedidor',
            name='cad_adm',
            field=models.OneToOneField(to='periciaapp.VerificacaoCadAdm', verbose_name='Código do cadastro Administrativo'),
        ),
        migrations.AlterField(
            model_name='verificacaorequisitosmetrologicos',
            name='req_tec',
            field=models.OneToOneField(to='periciaapp.VerificacaoRequisitosTecnicos', verbose_name='Código do requisito técnico'),
        ),
    ]
