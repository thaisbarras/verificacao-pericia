from django.conf.urls import include, url
from . import views
from .views import ListaPericia, ListaVerificacao, ListaAgendamento,\
    AddPericia, AddAgendamento, AddVerificacaoAdm, AddVerificacaoMedidor, AddVerificacaoRequisitosAdm, AddVerificacaoRequisitosTecnicos, AddVerificacaoRequisitosMetrologicos, DetalheVerificacao

urlpatterns = [
    url(r'^$', views.home, name='home'),

    #----------- Listas ----------
    url(r'^pericias/$', ListaPericia.as_view(), name='lista_pericia'),  
    url(r'^verificacoes/$', ListaVerificacao.as_view(), name='lista_verificacao'),
    url(r'^detalheveficicacao/$', DetalheVerificacao.as_view(), name='detalhe_verificacao'),
    url(r'^agendamentos/$', ListaAgendamento.as_view(), name='lista_agendamento'),

    #---------- Adicoes ----------
    url(r'^add_pericia/$', AddPericia.as_view(), name='add_pericia'),
    url(r'^add_agendamento/$', AddAgendamento.as_view(), name='add_agendamento'),
    url(r'^add_verificacao_adm/$', AddVerificacaoAdm.as_view(), name='add_verificacao_adm'),
    url(r'^add_verificacao_medidor/$', AddVerificacaoMedidor.as_view(), name='add_verificacao_medidor'),
    url(r'^add_verificacao_requisitosadm/$', AddVerificacaoRequisitosAdm.as_view(), name='add_verificacao_requisitosadm'),
    url(r'^add_verificacao_requisitostecnicos/$', AddVerificacaoRequisitosTecnicos.as_view(), name='add_verificacao_requisitostecnicos'),
    url(r'^add_verificacao_requisitosmetrologicos/$', AddVerificacaoRequisitosMetrologicos.as_view(), name='add_verificacao_requisitosmetrologicos'),
    
    #url(r'^contact/$', 'pericia.views.pericia_contact', name='contact'),
    #url(r'^protected/$', 'pericia.views.protected_view', name='protected'),
    #url(r'^accounts/login/$', 'message'),
]
    
