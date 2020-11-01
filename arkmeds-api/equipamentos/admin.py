from django.contrib import admin

from .models import (ChamadoEquipamento, Empresa, Equipamento, Proprietario,
                     ResponsavelTecnico, TipoEquipamento)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ['id']


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    search_fields = ['id']


@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    search_fields = ['id']


@admin.register(TipoEquipamento)
class TipoEquipamentoAdmin(admin.ModelAdmin):
    search_fields = ['id']


@admin.register(ResponsavelTecnico)
class ResponsavelTecnicoAdmin(admin.ModelAdmin):
    search_fields = ['id']


@admin.register(ChamadoEquipamento)
class ChamadoEquipamentoTecnicoAdmin(admin.ModelAdmin):
    search_fields = ['id']
