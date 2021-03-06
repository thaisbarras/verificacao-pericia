# -*- encoding: utf8 -*-
#from pericia.models import VerificacaoCadAdm
#from django.template.context import RequestContext
#from django.shortcuts import render, redirect, render_to_response, get_object_or_404
#from pericia.forms import FormItemPericia
#from django.http.response import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Pericia, VerificacaoCadAdm, VerificacaoCadMedidor, VerificacaoRequisitosTecnicos,\
    VerificacaoRequisitosAdm, VerificacaoRequisitosMetrologicos, AgendamentoModel, Verificacao
#from vanilla import CreateView
from .forms import ProcedimentoPericiaContactForm,\
    ProcedimentoPericiaForm, PreliminaresInspecaoForm, VerificacaoCadAdmForm, AgendamentoForm, VerificacaoForm
from django.views.generic.list import ListView
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.template.context import RequestContext
from django.views.generic import DetailView
from .forms import RequisitosAdmForm, RequisitosTecnicosForm


def home(request):
    return render(request, 'home.html')

#----------------------------------------------------------------
class DetalheVerificacao(DetailView):
    model = VerificacaoCadAdm
    #Template_name = 'periciaapp/detalhe_verificacao.html'


#-------------------------------
class ListaPericia(ListView):
        template_name = 'periciaapp/list_pericia.html'
        model = Pericia
        #fields = ['numero_pericia', 'verificacao', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor']
        context_object = 'verificacao'
        
class ListaVerificacao(ListView):
        template_name = 'periciaapp/list_verificacao.html'
        model = Verificacao
        form_class = VerificacaoForm
        #fields = ['numero_pericia', 'verificacao', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor']
        context_object = 'id_verificacao'

class ListaAgendamento (ListView):
    template_name = 'periciaapp/list_agendamentos.html'
    model = AgendamentoModel
    context_object = 'agendamento'

# ---------------------------------------- ADD ----------------------------------------
class AddPericia(CreateView):
    template_name = 'periciaapp/add_pericia.html'
    model = Pericia
    fields = '__all__'#['verificacao', 'image_pericia', 'data_pericia', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor', 'suporte_parafuso', 'circuito_corrente', 'circuito_tensao', 'mostrador', 'placa_identficacao', 'placa_circuito_impresso_componetes', 'outros', 'involucro_devolucao', 'pendencias', 'obs']
    success_url = reverse_lazy('lista_pericia')


class AddAgendamento(CreateView): 
    template_name = 'periciaapp/add_agendamento.html'
    model = AgendamentoModel
    form_class = AgendamentoForm
    #fields = '__all__'
    success_url = reverse_lazy('lista_agendamento')

 
class AddVerificacaoAdm(CreateView): 
    template_name = 'periciaapp/add_verificacao_adm.html'
    model = VerificacaoCadAdm
    form_class = VerificacaoCadAdmForm
    #fields = ['processo', 'data_verificacao', 'local', 'temperatura_ambiente', 'usuario', 'proprietario', 'requerente', 'tecnico_verificacao', 'equipamentos_utilizados']
    success_url = reverse_lazy('add_verificacao_medidor')
    

class AddVerificacaoMedidor(CreateView): 
    template_name = 'periciaapp/add_verificacao_medidor.html'
    model = VerificacaoCadMedidor
    #fields = ['numero_do_processo', 'medidor', 'tipo_medidor', 'classe_do_medidor', 'numero_de_elementos', 'numero_de_fios', 'tensao_nominal', 'corrente_nominal_max_a', 'frequencia_nominal', 'constante', 'ano_de_fabricante', 'identificacao', 'leitura_inicial_medidor', 'leitura_final_medidor']
    fields = '__all__'
    success_url = reverse_lazy('add_verificacao_requisitosadm')

class AddVerificacaoRequisitosAdm(CreateView):    
    template_name = 'periciaapp/add_verificacao_requisitosadm.html'
    model = VerificacaoRequisitosAdm
    form_class = RequisitosAdmForm
    #fields = '__all__'#['numero_do_processo', 'involucro', 'numero_involucro', 'condicao_involucro', 'toi', 'idtoi', 'preenchimento_toi', 'integridade_lacre', 'image_lacre', 'image_medidor','inspecao_visual', 'dado_placa', 'dimensao_medidor', 'plano_selagem', 'obs_inspecao_visual']
    success_url = reverse_lazy('add_verificacao_requisitostecnicos')

class AddVerificacaoRequisitosTecnicos(CreateView):    
    template_name = 'periciaapp/add_verificacao_requisitostecnicos.html'
    model = VerificacaoRequisitosTecnicos
    form_class = RequisitosTecnicosForm
    #fields = ['ensaio_marcha_vazio', 'resultado_ensaio_marcha_vazio', 'obs_ensaio_marcha_vazio', 'ensaio_mostrador', 'resultado_ensaio_mostrador', 'obs_ensaio_mostrador', 'ensaio_exatidao', 'resultado_ensaio_ensaio', 'obs_ensaio_exatidao']
    success_url = reverse_lazy('add_verificacao_requisitosmetrologicos')

class AddVerificacaoRequisitosMetrologicos(CreateView):    
    template_name = 'periciaapp/add_verificacao_requisitosmetrologicos.html'
    model = VerificacaoRequisitosMetrologicos
    #fields = ['energia_ativa_tensao', 'energia_ativa_corrente', 'energia_ativa_cos', 'energia_ativa_elementos', 'energia_ativa_erro', 'energia_ativa_erro_max', 'energia_reativa_tensao', 'energia_reativa_corrente', 'energia_reativa_cos', 'energia_reativa_elementos', 'energia_reativa_erro', 'energia_reativa_erro_max']
    fields = '__all__'
    success_url = reverse_lazy('lista_verificacao')

