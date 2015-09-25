# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('codigo_agendamento', models.CharField(max_length=10)),
                ('data_retirada', models.DateTimeField(default=datetime.datetime(2015, 9, 25, 9, 23, 41, 833579))),
                ('data_visita_do_usuario', models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 25, 9, 23, 41, 833579))),
                ('usuario_compareceu', models.CharField(max_length=50, choices=[('sim', 'sim'), ('nao', 'nao')])),
                ('observacoes', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['codigo_agendamento'],
                'verbose_name_plural': 'agendamentos',
                'verbose_name': 'agendamento',
            },
        ),
        migrations.CreateModel(
            name='CadEquipamento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('equipamento_calibrado', models.CharField(max_length=20)),
                ('data_calibracao', models.DateTimeField()),
            ],
            options={
                'ordering': ['equipamento_calibrado'],
                'verbose_name_plural': 'equipamentos',
                'verbose_name': 'equipamento',
            },
        ),
        migrations.CreateModel(
            name='CadMedidor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fabricante_marca_medidor', models.CharField(max_length=20)),
                ('modelo_medidor', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['fabricante_marca_medidor'],
                'verbose_name_plural': 'medidores',
                'verbose_name': 'medidor',
            },
        ),
        migrations.CreateModel(
            name='CadProprietario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('representante_legal', models.CharField(max_length=50)),
                ('cpf_cnpf_representante', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'proprietarios',
                'verbose_name': 'proprietario',
            },
        ),
        migrations.CreateModel(
            name='CadRequerente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'requerentes',
                'verbose_name': 'requerente',
            },
        ),
        migrations.CreateModel(
            name='CadTecnico',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome_tecnico', models.CharField(max_length=20)),
                ('identificacao_tecnico', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['nome_tecnico'],
                'verbose_name_plural': 'tecnicos',
                'verbose_name': 'tecnico',
            },
        ),
        migrations.CreateModel(
            name='CadUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'usuarios',
                'verbose_name': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Pericia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('data_pericia', models.DateTimeField()),
                ('tampa_medidor', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('tampa quebrada', 'tampa quebrada'), ('tampa perfurada', 'tampa perfurada'), ('tampa deformada', 'tampa deformada'), ('sem tampa', 'sem tampa'), ('Outros', 'Outros')])),
                ('base_medidor', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('base quebrada', 'base quebrada'), ('base perfurada', 'base perfurada'), ('base deformada', 'base deformada'), ('base adulterada', 'base adulterada'), ('Outros', 'Outros')])),
                ('bloco_terminais_medidor', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('bloco de terminais quebrada', 'bloco de terminais quebrada'), ('ausencia de parafuso', 'ausencia de parafuso'), ('parafuso oxidado', 'parafuso oxidado'), ('Terminais de prova abertos', 'Terminais de prova abertos'), ('Outros', 'Outros')])),
                ('suporte_parafuso', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('nao aplicavel', 'nao aplicavel'), ('suporte perfurado', 'suporte perfurado'), ('suporte deformado', 'suporte deformado'), ('material de gaveta deteriorado', 'material de gaveta deteriorado'), ('Outros', 'Outros')])),
                ('circuito_corrente', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('curto circuito', 'curto circuito'), ('fio rompido', 'fio rompido'), ('Outros', 'Outros')])),
                ('circuito_tensao', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('descontinuidade', 'descontinuidade'), ('fio rompido', 'fio rompido'), ('introducao de componentes', 'introducao de componentes'), ('Outros', 'Outros')])),
                ('mostrador', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('desconectado ou deslocado', 'desconectado ou deslocado '), ('mostrador danificada ', 'mostrador modificado'), ('engrenagens danificadas', 'engrenagens danificadas '), ('mostrador apagado ', 'mostrador apagado'), ('segmentos defeituosos', 'segmentos defeituosos'), ('noo indica grandeza', 'noo indica grandeza'), ('outros', 'outros')])),
                ('placa_identficacao', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('impressao adulterada', 'impressao adulterada'), ('outros', 'outros')])),
                ('placa_circuito_impresso_componetes', models.CharField(max_length=50, choices=[('conforme', 'conforme'), ('introducao de componentes', 'introducao de componentes'), ('conforme', 'conforme'), ('Retirada de componentes', 'Retirada de componentes'), ('Trilhas raspadas', 'Trilhas raspadas'), ('curto circuito', 'curto circuito'), ('introdução de circuitos', 'introdução de circuitos'), ('soldas defeituosas', 'soldas defeituosas'), ('outros', 'outros')])),
                ('outros', models.CharField(max_length=60, choices=[('nao aplicavel', 'nao aplicavel'), ('presenca de corpo estranho no interior do medidor', 'presenca de corpo estranho no interior do medidor'), ('presenca de sujeira no interior do medidor', 'presenca de sujeira no interior do medidor'), ('presenca de insetos no interior do medidor', 'presenca de insetos no interior do medidor'), ('botoes danificados', 'botoes danificados'), ('outros', 'outros')])),
                ('involucro_devolucao', models.BooleanField(verbose_name='possui? ')),
                ('pendencias', models.BooleanField(verbose_name='possui? ')),
                ('obs', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'ordering': ['verificacao'],
                'verbose_name_plural': 'pericias',
                'verbose_name': 'pericia',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadAdm',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('processo', models.CharField(max_length=10)),
                ('data_verificacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_toi', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('local', models.CharField(max_length=100)),
                ('temperatura_ambiente', models.CharField(max_length=10)),
                ('requerente', models.CharField(max_length=50, choices=[('usuario', 'usuario'), ('proprietário', 'proprietario'), ('orgao judicial', 'orgao judicial'), ('outros', 'outros')])),
            ],
            options={
                'ordering': ['processo'],
                'verbose_name_plural': 'verificacoesadm',
                'verbose_name': 'verificacaoadm',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadMedidor',
            fields=[
                ('numero_do_processo', models.OneToOneField(to='periciaapp.VerificacaoCadAdm', serialize=False, primary_key=True)),
                ('tipo_medidor', models.CharField(max_length=30, choices=[('medidor_eletroeletronico', 'medidor_eletroeletronico'), ('medidor_eletromecanico', 'medidor_eletromecanico')])),
                ('classe_do_medidor', models.CharField(max_length=10)),
                ('numero_de_elementos', models.CharField(max_length=10)),
                ('numero_de_fios', models.CharField(max_length=10)),
                ('tensao_nominal', models.CharField(max_length=10)),
                ('corrente_nominal_max_a', models.CharField(max_length=10)),
                ('frequencia_nominal', models.CharField(max_length=10)),
                ('constante', models.CharField(max_length=10)),
                ('ano_de_fabricante', models.CharField(max_length=10)),
                ('identificacao', models.CharField(max_length=10)),
                ('leitura_inicial_medidor', models.CharField(max_length=10)),
                ('leitura_final_medidor', models.CharField(max_length=10)),
                ('medidor', models.ForeignKey(to='periciaapp.CadMedidor', related_name='medidor')),
            ],
            options={
                'ordering': ['medidor'],
                'verbose_name_plural': 'cadmedidores',
                'verbose_name': 'cadmedidor',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosAdm',
            fields=[
                ('numero_do_processo', models.OneToOneField(to='periciaapp.VerificacaoCadAdm', serialize=False, primary_key=True)),
                ('involucro', models.BooleanField(verbose_name='possui involucro: ')),
                ('numero_involucro', models.CharField(max_length=10, blank=True)),
                ('condicao_involucro', models.CharField(max_length=30, choices=[('conforme', 'conforme'), ('perfurado', 'perfurado'), ('lacre violado', 'lacre violado'), ('outros', 'outros')])),
                ('toi', models.BooleanField(verbose_name='possui toi: ')),
                ('idtoi', models.CharField(max_length=50, blank=True)),
                ('preenchimento_toi', models.CharField(max_length=20, choices=[('conforme', 'conforme'), ('incompleto', 'incompleto'), ('sem assinatura', 'sem assinatura'), ('outros', 'outros')])),
                ('integridade_lacre', models.CharField(max_length=20, choices=[('conforme', 'conforme'), ('ausente', 'ausente'), ('travas danificadas', 'travas danificadas'), ('arame rompido', 'arame rompido'), ('arame incorreto', 'arame incorreto'), ('ponto ligacao rompido', 'ponto ligacao rompido'), ('outros', 'outros')])),
                ('inspecao_visual', models.BooleanField(verbose_name='realizado? ')),
                ('dado_placa', models.BooleanField(verbose_name='esta conforme? ')),
                ('dimensao_medidor', models.BooleanField(verbose_name='esta conforme? ')),
                ('plano_selagem', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_inspecao_visual', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosMetrologicos',
            fields=[
                ('numero_do_processo', models.OneToOneField(to='periciaapp.VerificacaoCadAdm', serialize=False, primary_key=True)),
                ('energia_ativa_tensao', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_corrente', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_cos', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_elementos', models.CharField(max_length=20, blank=True)),
                ('energia_ativa_erro', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_erro_max', models.CharField(max_length=20, blank=True)),
                ('energia_reativa_tensao', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_corrente', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_cos', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_elementos', models.CharField(max_length=20, blank=True)),
                ('energia_reativa_erro', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_erro_max', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': ['numero_do_processo'],
                'verbose_name_plural': 'verificacoes',
                'verbose_name': 'verificacao',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosTecnicos',
            fields=[
                ('numero_do_processo', models.OneToOneField(to='periciaapp.VerificacaoCadAdm', serialize=False, primary_key=True)),
                ('ensaio_marcha_vazio', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_marcha_vazio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_marcha_vazio', models.CharField(max_length=50, blank=True)),
                ('ensaio_mostrador', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_mostrador', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_mostrador', models.CharField(max_length=50, blank=True)),
                ('ensaio_exatidao', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_ensaio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_exatidao', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='equipamentos_utilizados',
            field=models.ManyToManyField(to='periciaapp.CadEquipamento', related_name='equipamento'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='proprietario',
            field=models.ForeignKey(to='periciaapp.CadProprietario'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='tecnico_verificacao',
            field=models.ForeignKey(to='periciaapp.CadTecnico', related_name='tecnico'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='usuario',
            field=models.ForeignKey(to='periciaapp.CadUsuario'),
        ),
        migrations.AddField(
            model_name='pericia',
            name='verificacao',
            field=models.ForeignKey(to='periciaapp.VerificacaoCadAdm'),
        ),
        migrations.AddField(
            model_name='agendamentomodel',
            name='codigo_usuario',
            field=models.ForeignKey(to='periciaapp.CadUsuario'),
        ),
    ]
