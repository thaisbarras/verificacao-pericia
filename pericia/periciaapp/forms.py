# -*- coding: utf-8 -*-
from django import forms
from periciaapp.models import Pericia, CadEquipamento, VerificacaoCadAdm
from django.forms.widgets import Textarea, CheckboxSelectMultiple, CheckboxInput,\
    SelectMultiple, RadioSelect, Select
from django.forms.extras.widgets import SelectDateWidget
from msilib import RadioButtonGroup

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
            'requerente': RadioSelect,
            'data_verificacao': SelectDateWidget,
            'equipamentos_utilizados': CheckboxSelectMultiple, 
        }
    
    def ini_processo(self):
        processo = '52600.'
        
        
        


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
        
        fields = ['processo', 'data_verificacao', 'local', 'temperatura_ambiente', 'usuario', 'proprietario', 'requerente', 'tecnico_verificacao', 'equipamentos_utilizados']
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
