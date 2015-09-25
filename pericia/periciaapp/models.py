# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.admin.filters import ChoicesFieldListFilter
from django.db.models.fields import AutoField
from enum import unique
from django.db.models.fields.files import ImageField
from _datetime import timezone, date
from django.utils import timezone
import datetime
from itertools import repeat


class CadRequerente(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 40)
    cpf_cnpj = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'requerente'
        verbose_name_plural = 'requerentes'
    
    def __str__(self):
        return self.nome
    
class CadUsuario(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 40)
    cpf_cnpj = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
    
    def __str__(self):
        return self.nome


class CadProprietario(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 40)
    cpf_cnpj = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 20)
    email = models.EmailField()
    representante_legal = models.CharField(max_length = 50)
    cpf_cnpf_representante = models.CharField(max_length = 20)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'proprietario'
        verbose_name_plural = 'proprietarios'
    
    def __str__(self):
        return self.nome

class CadMedidor(models.Model):#sistema do Alexsander
    fabricante_marca_medidor = models.CharField(max_length = 20)
    modelo_medidor = models.CharField(max_length = 20)
    
    class Meta:
        ordering = ['fabricante_marca_medidor']
        verbose_name = 'medidor'
        verbose_name_plural = 'medidores'
    
    def __str__(self):
        return self.fabricante_marca_medidor
    
class CadTecnico(models.Model):#sistema da Messias
    nome_tecnico = models.CharField(max_length = 20)
    identificacao_tecnico = models.CharField(max_length = 20)

    class Meta:
        ordering = ['nome_tecnico']
        verbose_name = 'tecnico'
        verbose_name_plural = 'tecnicos'
    def __str__(self):
        return self.nome_tecnico
    

class CadEquipamento(models.Model):#sistema da Messias
    equipamento_calibrado = models.CharField(max_length = 20)
    data_calibracao = models.DateTimeField(auto_now=False)
    class Meta:
        ordering = ['equipamento_calibrado']
        verbose_name = 'equipamento'
        verbose_name_plural = 'equipamentos'
    def __str__(self):
        return self.equipamento_calibrado


class AgendamentoModel(models.Model):
    codigo_agendamento = models.CharField(max_length = 10)
    codigo_usuario = models.ForeignKey(CadUsuario)
    data_retirada = models.DateTimeField(default=datetime.datetime.now())
    data_visita_do_usuario = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    usuario_compareceu = models.CharField(choices=(
            ('sim', 'sim'),
            ('nao', 'nao'),
            ),
            max_length=50
    )
    observacoes = models.CharField(max_length = 100)

    class Meta:
        ordering = ['codigo_agendamento']
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'
    
    def __str__(self):
        return self.agendamento
    
    
class VerificacaoCadAdm(models.Model):
    processo = models.CharField(max_length = 10)
    data_verificacao = models.DateTimeField(default=timezone.now)
    data_toi = models.DateTimeField(default=timezone.now, blank=True)
    local = models.CharField(max_length = 100)
    temperatura_ambiente = models.CharField(max_length = 10)   
    usuario = models.ForeignKey(CadUsuario)
    proprietario = models.ForeignKey(CadProprietario)
    requerente = models.CharField(choices=(
            ('usuario', 'usuario'),
            ('proprietário', 'proprietario'),
            ('orgao judicial', 'orgao judicial'),
            ('outros', 'outros'),
        ),
        max_length=50
    )
    tecnico_verificacao = models.ForeignKey(CadTecnico, related_name='tecnico')
    equipamentos_utilizados = models.ManyToManyField(CadEquipamento, related_name='equipamento')
     
    class Meta:
        ordering = ['processo']
        verbose_name = 'verificacaoadm'
        verbose_name_plural = 'verificacoesadm'
    
    def __str__(self):
        return self.processo

class VerificacaoCadMedidor(models.Model):
    numero_do_processo = models.OneToOneField(VerificacaoCadAdm, primary_key=True)
    medidor = models.ForeignKey(CadMedidor, related_name='medidor')
    tipo_medidor = models.CharField(choices=(
            ('medidor_eletroeletronico', 'medidor_eletroeletronico'),
            ('medidor_eletromecanico', 'medidor_eletromecanico'),
        ),
        max_length=30
    )
    classe_do_medidor = models.CharField(max_length = 10)
    numero_de_elementos = models.CharField(max_length = 10)
    numero_de_fios = models.CharField(max_length = 10)
    tensao_nominal = models.CharField(max_length = 10)
    corrente_nominal_max_a = models.CharField(max_length = 10)
    frequencia_nominal = models.CharField(max_length = 10)
    constante = models.CharField(max_length = 10)
    ano_de_fabricante = models.CharField(max_length = 10)
    identificacao = models.CharField(max_length = 10)
    
    leitura_inicial_medidor = models.CharField(max_length = 10)
    leitura_final_medidor = models.CharField(max_length = 10)
    
    class Meta:
        ordering = ['medidor']
        verbose_name = 'cadmedidor'
        verbose_name_plural = 'cadmedidores'
        
    def __str__(self):
        return self.medidor
    
class VerificacaoRequisitosAdm(models.Model):
    numero_do_processo = models.OneToOneField(VerificacaoCadAdm, primary_key=True)
    involucro = models.BooleanField('possui involucro: ')
    numero_involucro = models.CharField(max_length = 10, blank = True)
    condicao_involucro = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('perfurado', 'perfurado'),
            ('lacre violado', 'lacre violado'),
            ('outros', 'outros'),
        ),
        max_length=30
    )
    toi = models.BooleanField('possui toi: ')
    idtoi = models.CharField(max_length = 50, blank = True)
    preenchimento_toi = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('incompleto', 'incompleto'),
            ('sem assinatura', 'sem assinatura'),
            ('outros', 'outros'),
        ),
        max_length=20
    )
    
    integridade_lacre = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('ausente', 'ausente'),
            ('travas danificadas', 'travas danificadas'),
            ('arame rompido', 'arame rompido'),
            ('arame incorreto', 'arame incorreto'),
            ('ponto ligacao rompido', 'ponto ligacao rompido'),
            ('outros', 'outros'),
        ),
        max_length=20
    )
    #image_lacre = models.ImageField(upload_to = 'imagens/verificacao/lacre/', blank = True)
    #image_medidor = models.ImageField(upload_to = 'imagens/verificacao/medidor/', blank = True)
    
    inspecao_visual = models.BooleanField('realizado? ')
    dado_placa = models.BooleanField('esta conforme? ')
    dimensao_medidor = models.BooleanField('esta conforme? ')
    plano_selagem = models.BooleanField('esta conforme? ')
    obs_inspecao_visual = models.CharField(max_length = 50, blank = True)
    
class VerificacaoRequisitosTecnicos(models.Model):
    numero_do_processo = models.OneToOneField(VerificacaoCadAdm, primary_key=True)
    ensaio_marcha_vazio = models.BooleanField('realizado? ')
    resultado_ensaio_marcha_vazio = models.BooleanField('esta conforme? ')
    obs_ensaio_marcha_vazio = models.CharField(max_length = 50, blank = True)
    
    ensaio_mostrador = models.BooleanField('realizado? ')
    resultado_ensaio_mostrador = models.BooleanField('esta conforme? ')
    obs_ensaio_mostrador = models.CharField(max_length = 50, blank = True)
    
    ensaio_exatidao = models.BooleanField('realizado? ')
    resultado_ensaio_ensaio = models.BooleanField('esta conforme? ')
    obs_ensaio_exatidao = models.CharField(max_length = 50, blank = True)
    
class VerificacaoRequisitosMetrologicos(models.Model):
    numero_do_processo = models.OneToOneField(VerificacaoCadAdm, primary_key=True)
    energia_ativa_tensao = models.CharField(max_length = 10, blank = True)
    energia_ativa_corrente = models.CharField(max_length = 10, blank = True)
    energia_ativa_cos = models.CharField(max_length = 10, blank = True)
    energia_ativa_elementos = models.CharField(max_length = 20, blank = True) 
    energia_ativa_erro = models.CharField(max_length = 10, blank = True)
    energia_ativa_erro_max = models.CharField(max_length = 20, blank = True)
    energia_reativa_tensao = models.CharField(max_length = 10, blank = True)
    energia_reativa_corrente = models.CharField(max_length = 10, blank = True)
    energia_reativa_cos = models.CharField(max_length = 10, blank = True)
    energia_reativa_elementos = models.CharField(max_length = 20, blank = True) 
    energia_reativa_erro = models.CharField(max_length = 10, blank = True)
    energia_reativa_erro_max = models.CharField(max_length = 20, blank = True)
    
    
    class Meta:
        ordering = ['numero_do_processo']
        verbose_name = 'verificacao'
        verbose_name_plural = 'verificacoes'
    
    def __str__(self):
        return self.numero_do_processo
    
    #def contar_verificacao(self):
        #return self.pericia.count()
    
    #def detalhe_pericia(self):
        #return u"/pericias/%i" % self.id
    
class Pericia(models.Model):
    verificacao = models.ForeignKey(VerificacaoCadAdm)
    #image_pericia = models.ImageField(upload_to = 'imagens/pericia/medidor/', blank = True)
    #tecnico_pericia = models.ForeignKey(CadTecnico, related_name='tecnico')
    data_pericia = models.DateTimeField()   
    tampa_medidor = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('tampa quebrada', 'tampa quebrada'),
            ('tampa perfurada', 'tampa perfurada'),
            ('tampa deformada', 'tampa deformada'),
            ('sem tampa', 'sem tampa'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    )
    base_medidor = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('base quebrada', 'base quebrada'),
            ('base perfurada', 'base perfurada'),
            ('base deformada', 'base deformada'),
            ('base adulterada', 'base adulterada'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    )
    bloco_terminais_medidor = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('bloco de terminais quebrada', 'bloco de terminais quebrada'),
            ('ausencia de parafuso', 'ausencia de parafuso'),
            ('parafuso oxidado', 'parafuso oxidado'),
            ('Terminais de prova abertos', 'Terminais de prova abertos'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    )   
    suporte_parafuso = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('nao aplicavel', 'nao aplicavel'),
            ('suporte perfurado', 'suporte perfurado'),
            ('suporte deformado', 'suporte deformado'),
            ('material de gaveta deteriorado', 'material de gaveta deteriorado'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    ) 
    circuito_corrente = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('curto circuito', 'curto circuito'),
            ('fio rompido', 'fio rompido'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    ) 
    circuito_tensao = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('descontinuidade', 'descontinuidade'),
            ('fio rompido', 'fio rompido'),
            ('introducao de componentes', 'introducao de componentes'),
            ('Outros', 'Outros'),
        ),
        max_length=50
    )
    mostrador = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('desconectado ou deslocado', 'desconectado ou deslocado '),
            ('mostrador danificada ', 'mostrador modificado'),
            ('engrenagens danificadas', 'engrenagens danificadas '),
            ('mostrador apagado ', 'mostrador apagado'),
            ('segmentos defeituosos', 'segmentos defeituosos'),
            ('noo indica grandeza', 'noo indica grandeza'),
            ('outros', 'outros'),
        ),
        max_length=50
    ) 
    placa_identficacao = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('impressao adulterada', 'impressao adulterada'),
            ('outros', 'outros'),
        ),
        max_length=50
    )
    placa_circuito_impresso_componetes = models.CharField(choices=(
            ('conforme', 'conforme'),
            ('introducao de componentes', 'introducao de componentes'),
            ('conforme', 'conforme'),
            ('Retirada de componentes', 'Retirada de componentes'),
            ('Trilhas raspadas', 'Trilhas raspadas'),
            ('curto circuito', 'curto circuito'),
            ('introdução de circuitos', 'introdução de circuitos'),
            ('soldas defeituosas', 'soldas defeituosas'),
            ('outros', 'outros'),
        ),
        max_length=50
    )
    outros = models.CharField(choices=(
            ('nao aplicavel', 'nao aplicavel'),
            ('presenca de corpo estranho no interior do medidor', 'presenca de corpo estranho no interior do medidor'),
            ('presenca de sujeira no interior do medidor', 'presenca de sujeira no interior do medidor'),
            ('presenca de insetos no interior do medidor', 'presenca de insetos no interior do medidor'),
            ('botoes danificados', 'botoes danificados'),
            ('outros', 'outros'),
        ),
        max_length=60
    )
    involucro_devolucao = models.BooleanField('possui? ')
    pendencias = models.BooleanField('possui? ')
    obs = models.CharField(max_length = 500, blank = True)
    
    class Meta:
        ordering = ['verificacao']
        verbose_name = 'pericia'
        verbose_name_plural = 'pericias'
    
    def __str__(self):
        return self.tampa_medidor
