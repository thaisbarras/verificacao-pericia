from django.contrib import admin
from .models import CadRequerente, CadUsuario, CadProprietario, CadMedidor, CadTecnico, CadEquipamento, AgendamentoModel, VerificacaoCadAdm, VerificacaoCadMedidor, VerificacaoRequisitosAdm, VerificacaoRequisitosTecnicos, VerificacaoRequisitosMetrologicos, Pericia

admin.site.register(CadRequerente)
admin.site.register(CadUsuario)
admin.site.register(CadProprietario)
admin.site.register(CadMedidor)
admin.site.register(CadTecnico)
admin.site.register(CadEquipamento)
admin.site.register(AgendamentoModel)
admin.site.register(VerificacaoCadAdm)
admin.site.register(VerificacaoCadMedidor)
admin.site.register(VerificacaoRequisitosAdm)
admin.site.register(VerificacaoRequisitosTecnicos)
admin.site.register(VerificacaoRequisitosMetrologicos)
admin.site.register(Pericia)
