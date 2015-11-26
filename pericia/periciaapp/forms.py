# -*- coding: utf-8 -*-
from django import forms
from .models import Pericia, CadEquipamento, VerificacaoCadAdm, AgendamentoModel
from django.forms.widgets import Textarea, CheckboxSelectMultiple, CheckboxInput,\
    SelectMultiple, RadioSelect, Select, DateInput, TextInput
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
from django.forms.fields import BooleanField
from .models import VerificacaoRequisitosAdm, VerificacaoRequisitosTecnicos, VerificacaoRequisitosMetrologicos, Verificacao
#from msilib import RadioButtonGroup



class AgendamentoForm(forms.ModelForm):
    #data_da_retirada = forms.DateField(widget=widgets.AdminDateWidget)
    #data_da_retirada = forms.DateField(widget=SelectDateWidget)
    #data_da_visita_do_usuario = forms.DateField(widget=SelectDateWidget)
    class Meta:    
        model = AgendamentoModel
        fields = '__all__'
        widgets = {
            'data_da_retirada': SelectDateWidget,
            'data_da_visita_do_usuario': SelectDateWidget,
            'usuario_compareceu': forms.RadioSelect,
            'observacoes': Textarea,
               }

        

class ProcedimentoPericiaContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    
class VerificacaoCadAdmForm(forms.ModelForm):
    
    class Meta:
        model = VerificacaoCadAdm
        fields = '__all__'
        widgets = {
            'data_verificacao': SelectDateWidget,
            'data_toi': SelectDateWidget,
            'equipamentos_utilizados': CheckboxSelectMultiple, 
        }
    
    def ini_processo(self):
        processo = '52600.'
        
        
class RequisitosAdmForm(forms.ModelForm):
      class Meta:
        model = VerificacaoRequisitosAdm
        fields = '__all__'
        widgets = {
            'involucro': forms.RadioSelect,
            'toi': forms.RadioSelect,
            'inspecao_visual': forms.RadioSelect,
            'dado_placa': forms.RadioSelect,
            'dimensao_medidor': forms.RadioSelect,
            'plano_selagem': forms.RadioSelect,
            'obs_inspecao_visual': Textarea,
            }
        
class RequisitosTecnicosForm(forms.ModelForm):
      class Meta:
        model = VerificacaoRequisitosTecnicos
        fields = '__all__'
        widgets = {
            'ensaio_marcha_vazio': forms.RadioSelect,
            'resultado_ensaio_marcha_vazio': forms.RadioSelect,
            'ensaio_mostrador': forms.RadioSelect,
            'resultado_ensaio_mostrador': forms.RadioSelect,
            'ensaio_exatidao': forms.RadioSelect,
            'resultado_ensaio_ensaio': forms.RadioSelect,
            'obs_ensaio_marcha_vazio': Textarea,
            'obs_ensaio_mostrador': Textarea,
            'obs_ensaio_exatidao': Textarea,
            }


class VerificacaoForm(forms.ModelForm):
    
    class Meta:
        model = Verificacao
        fields = '__all__'

class ProcedimentoPericiaForm(forms.ModelForm):
    
    class Meta:
        model = Pericia
        fields = '__all__'
        image_pericia = forms.ImageField()
        widgets = {
            'obs': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        per = ((0, 'Nao'), (1, 'Sim'))
        
        involucro_devolucao = forms.TypedChoiceField(choices = per, widget=forms.RadioSelect, coerce=int)
        pendencias = forms.TypedChoiceField(choices = per, widget=forms.RadioSelect, coerce=int)
        
        


class PreliminaresInspecaoForm(forms.ModelForm):
    
    
    class Meta:
        model = VerificacaoCadAdm
        
        fields = '__all__'
        '''
        data = forms.DateField()
        equipamento_utilzado = forms.ModelMultipleChoiceField(queryset=CadEquipamento.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
        involucro = forms.TypedChoiceField(label='Possui Involucro: ', choices = inv, widget=forms.RadioSelect, coerce=int)
        toi = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        image_lacre = forms.ImageField()
        image_medidor = forms.ImageField()
        inspecao_visual = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        dado_placa = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        dimensao_medidor = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        plano_selagem = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        ensaio_marcha_vazio = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        resultado_ensaio_marcha_vazio = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        ensaio_mostrador = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        resultado_ensaio_mostrador = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        ensaio_exatidao = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        resultado_ensaio_ensai = forms.TypedChoiceField(choices = inv, widget=forms.RadioSelect, coerce=int)
        
        involucro = (('conforme', 'conforme'), ('perfurado', 'perfurado'), ('lacre violado', 'lacre violado'), ('outros', 'outros'))
        condicao_involucro = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = involucro)
        widgets = {
                   'data' : forms.DateInput(format=('%d/%m/%Y'),
                                            attrs={'class':'myDateClass', 
                                            'placeholder':'dd/mm/aaaa'})
                   }
'''
        

"""class FormItemPericia(forms.ModelForm):
    class Meta:
        model = PreliminaresInspecao
        fields = ['involucro', 'idtoi', 'procedimento_toi']"""
