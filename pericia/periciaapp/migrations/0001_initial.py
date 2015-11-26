# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoModel',
            fields=[
                ('codigo_agendamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_da_retirada', models.DateTimeField(verbose_name='Data que o equipamento foi retirado da casa do usuário', default=django.utils.timezone.now)),
                ('data_da_visita_do_usuario', models.DateTimeField(verbose_name='Data que o Usuário deve visitar o laboratório', default=django.utils.timezone.now)),
                ('usuario_compareceu', models.BooleanField(verbose_name='Usuario compareceu no dia agendado?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('observacoes', models.CharField(max_length=100, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'agendamento',
                'verbose_name_plural': 'agendamentos',
                'ordering': ['codigo_agendamento'],
            },
        ),
        migrations.CreateModel(
            name='CadEquipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('equipamento_calibrado', models.CharField(max_length=20)),
                ('data_calibracao', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'equipamento',
                'verbose_name_plural': 'equipamentos',
                'ordering': ['equipamento_calibrado'],
            },
        ),
        migrations.CreateModel(
            name='CadMedidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fabricante_marca_medidor', models.CharField(max_length=20)),
                ('modelo_medidor', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'medidor',
                'verbose_name_plural': 'medidores',
                'ordering': ['fabricante_marca_medidor'],
            },
        ),
        migrations.CreateModel(
            name='CadProprietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('representante_legal', models.CharField(max_length=50)),
                ('cpf_cnpf_representante', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'proprietario',
                'verbose_name_plural': 'proprietarios',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CadRequerente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'requerente',
                'verbose_name_plural': 'requerentes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CadTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome_tecnico', models.CharField(max_length=20)),
                ('identificacao_tecnico', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'tecnico',
                'verbose_name_plural': 'tecnicos',
                'ordering': ['nome_tecnico'],
            },
        ),
        migrations.CreateModel(
            name='CadUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Pericia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                'verbose_name': 'pericia',
                'verbose_name_plural': 'pericias',
                'ordering': ['verificacao'],
            },
        ),
        migrations.CreateModel(
            name='Verificacao',
            fields=[
                ('id_verificacao', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'verificacao_voluntaria',
                'verbose_name_plural': 'verificacoes_voluntarias',
                'ordering': ['id_verificacao'],
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadAdm',
            fields=[
                ('id_cad_administrativo', models.AutoField(primary_key=True, serialize=False)),
                ('data_verificacao', models.DateTimeField(verbose_name='Data da verificação', default=django.utils.timezone.now)),
                ('data_toi', models.DateTimeField(verbose_name='Data do TOI', blank=True, default=django.utils.timezone.now)),
                ('local', models.CharField(verbose_name='Local da Realização da Verificação', max_length=100)),
                ('temperatura_ambiente', models.CharField(verbose_name='Temperatura do Ambiente', max_length=10)),
                ('requerente', models.CharField(verbose_name='Requerente da Verificação', max_length=50, choices=[('usuario', 'usuario'), ('proprietário', 'proprietario'), ('orgao judicial', 'orgao judicial'), ('outros', 'outros')])),
                ('codigo_agendamento', models.OneToOneField(to='periciaapp.AgendamentoModel')),
                ('equipamentos_utilizados', models.ManyToManyField(to='periciaapp.CadEquipamento', related_name='equipamento')),
                ('proprietario', models.ForeignKey(to='periciaapp.CadProprietario')),
                ('tecnico_verificacao', models.ForeignKey(to='periciaapp.CadTecnico', verbose_name='Técnico que realizou a verificação', related_name='tecnico')),
            ],
            options={
                'verbose_name': 'verificacaoadm',
                'verbose_name_plural': 'verificacoesadm',
                'ordering': ['id_cad_administrativo'],
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadMedidor',
            fields=[
                ('id_cad_medidor', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_medidor', models.CharField(verbose_name='Tipo do Medidor', max_length=30, choices=[('medidor_eletroeletronico', 'medidor_eletroeletronico'), ('medidor_eletromecanico', 'medidor_eletromecanico')])),
                ('classe_do_medidor', models.CharField(max_length=10)),
                ('numero_de_elementos', models.CharField(verbose_name='número de elementos', max_length=10, blank=True)),
                ('numero_de_fios', models.CharField(verbose_name='número de fios', max_length=10, blank=True)),
                ('tensao_nominal', models.CharField(verbose_name='tensão nominal', max_length=10, blank=True)),
                ('corrente_nominal_max_a', models.CharField(verbose_name='corrente nominal máxima (A)', max_length=10, blank=True)),
                ('frequencia_nominal', models.CharField(max_length=10)),
                ('constante', models.CharField(max_length=10)),
                ('ano_de_fabricante', models.CharField(max_length=10)),
                ('identificacao', models.CharField(max_length=10)),
                ('leitura_inicial_medidor', models.CharField(max_length=10)),
                ('leitura_final_medidor', models.CharField(max_length=10)),
                ('cad_adm', models.OneToOneField(to='periciaapp.VerificacaoCadAdm')),
                ('medidor', models.ForeignKey(related_name='medidor', to='periciaapp.CadMedidor')),
            ],
            options={
                'verbose_name': 'cadmedidor',
                'verbose_name_plural': 'cadmedidores',
                'ordering': ['medidor'],
            },
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosAdm',
            fields=[
                ('id_req_adm', models.AutoField(primary_key=True, serialize=False)),
                ('involucro', models.BooleanField(verbose_name='Possui Invólocro?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('numero_involucro', models.CharField(verbose_name='número do invóluvro', max_length=10, blank=True)),
                ('condicao_involucro', models.CharField(verbose_name='condição do Invólocro?', max_length=30, choices=[('conforme', 'conforme'), ('perfurado', 'perfurado'), ('lacre violado', 'lacre violado'), ('outros', 'outros')])),
                ('toi', models.BooleanField(verbose_name='Possui TOI?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('idtoi', models.CharField(verbose_name='Id do TOI', max_length=50, blank=True)),
                ('preenchimento_toi', models.CharField(verbose_name='Preenchimento do TOI?', max_length=20, choices=[('conforme', 'conforme'), ('incompleto', 'incompleto'), ('sem assinatura', 'sem assinatura'), ('outros', 'outros')])),
                ('integridade_lacre', models.CharField(verbose_name='Integridade do Lacre', max_length=20, choices=[('conforme', 'conforme'), ('ausente', 'ausente'), ('travas danificadas', 'travas danificadas'), ('arame rompido', 'arame rompido'), ('arame incorreto', 'arame incorreto'), ('ponto ligacao rompido', 'ponto ligacao rompido'), ('outros', 'outros')])),
                ('inspecao_visual', models.BooleanField(verbose_name='Foi Realizado inspeção visual?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('dado_placa', models.BooleanField(verbose_name='Dados da Placa está conforme?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('dimensao_medidor', models.BooleanField(verbose_name='Dimensão do medidor está conforme', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('plano_selagem', models.BooleanField(verbose_name='Plano Selagem está conforme?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('obs_inspecao_visual', models.CharField(verbose_name='Observações da Inspeção Visual?', max_length=100, blank=True)),
                ('cad_med', models.OneToOneField(to='periciaapp.VerificacaoCadMedidor', verbose_name='Código do cadastro do medidor')),
            ],
            options={
                'verbose_name': 'requisito_administrativo',
                'verbose_name_plural': 'requisitos_administrativos',
                'ordering': ['id_req_adm'],
            },
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosMetrologicos',
            fields=[
                ('id_req_met', models.AutoField(primary_key=True, serialize=False)),
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
                'verbose_name': 'requisito_metrologico',
                'verbose_name_plural': 'requisitos_metrologicos',
                'ordering': ['id_req_met'],
            },
        ),
        migrations.CreateModel(
            name='VerificacaoRequisitosTecnicos',
            fields=[
                ('id_req_tec', models.AutoField(primary_key=True, serialize=False)),
                ('ensaio_marcha_vazio', models.BooleanField(verbose_name='Ensaio Marcha Vazio realizado?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('resultado_ensaio_marcha_vazio', models.BooleanField(verbose_name='Resultado ensaio Marcha Vazio está conforme?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('obs_ensaio_marcha_vazio', models.CharField(max_length=50, blank=True)),
                ('ensaio_mostrador', models.BooleanField(verbose_name='Ensaio de mostrador realizado?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('resultado_ensaio_mostrador', models.BooleanField(verbose_name='Ensaio de Mostrador está conforme?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('obs_ensaio_mostrador', models.CharField(max_length=50, blank=True)),
                ('ensaio_exatidao', models.BooleanField(verbose_name='Ensaio de Exatidão está realizado?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('resultado_ensaio_ensaio', models.BooleanField(verbose_name='Ensaio de Exatidão está conforme?', default=True, choices=[(True, 'Sim'), (False, 'Não')])),
                ('obs_ensaio_exatidao', models.CharField(max_length=50, blank=True)),
                ('req_adm', models.OneToOneField(to='periciaapp.VerificacaoRequisitosAdm', verbose_name='Código do requisito administrativo')),
            ],
            options={
                'verbose_name': 'requisito_tecnico',
                'verbose_name_plural': 'requisitos_tecnicos',
                'ordering': ['id_req_tec'],
            },
        ),
        migrations.AddField(
            model_name='verificacaorequisitosmetrologicos',
            name='req_tec',
            field=models.OneToOneField(to='periciaapp.VerificacaoRequisitosTecnicos', verbose_name='Código do requisito metrológico'),
        ),
        migrations.AddField(
            model_name='verificacao',
            name='cad_administrativo',
            field=models.ForeignKey(to='periciaapp.VerificacaoCadAdm'),
        ),
        migrations.AddField(
            model_name='verificacao',
            name='cad_medidor',
            field=models.ForeignKey(to='periciaapp.VerificacaoCadMedidor'),
        ),
        migrations.AddField(
            model_name='verificacao',
            name='cad_req_adm',
            field=models.ForeignKey(to='periciaapp.VerificacaoRequisitosAdm'),
        ),
        migrations.AddField(
            model_name='verificacao',
            name='cad_req_met',
            field=models.ForeignKey(to='periciaapp.VerificacaoRequisitosMetrologicos'),
        ),
        migrations.AddField(
            model_name='verificacao',
            name='cad_req_tec',
            field=models.ForeignKey(to='periciaapp.VerificacaoRequisitosTecnicos'),
        ),
        migrations.AddField(
            model_name='pericia',
            name='verificacao',
            field=models.ForeignKey(to='periciaapp.VerificacaoCadAdm'),
        ),
        migrations.AddField(
            model_name='agendamentomodel',
            name='codigo_do_usuario',
            field=models.ForeignKey(to='periciaapp.CadUsuario'),
        ),
    ]
