from rest_framework import serializers

from .models import (ChamadoEquipamento, Empresa, Equipamento, Proprietario,
                     ResponsavelTecnico, TipoEquipamento)


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'tipo', 'nome', 'nome_fantasia', 'superior', 'cnpj',
                  'observacoes', 'contato', 'email', 'telefone1', 'ramal1', 'telefone2',
                  'ramal2', 'fax', 'cep', 'rua', 'numero', 'bairro', 'cidade', 'estado']


class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = ['id', 'nome', 'apelido']


class EquipamentoSerializer(serializers.ModelSerializer):
    proprietario = ProprietarioSerializer()

    class Meta:
        model = Equipamento
        fields = ['id', 'fabricante', 'modelo', 'patrimonio', 'numero_serie',
                  'identificacao', 'proprietario', 'tipo', 'qr_code']


class TipoEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipamento
        fields = ['id', 'descricao']


class ResposavelTecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsavelTecnico
        fields = ['id', 'has_avatar', 'nome',
                  'email', 'has_resp_tecnico', 'avatar']


class ChamadoEquipamentoSerializer(serializers.ModelSerializer):
    equipamento = EquipamentoSerializer()

    class Meta:
        model = ChamadoEquipamento
        fields = ['id', 'chamados', 'cor_prioridade', 'prioridade', 'get_prioridade',
                  'numero', 'get_solicitante', 'get_equipamento_servico', 'get_criticidde',
                  'tempo', 'tempo_fechamento', 'responsavel_str', 'get_resp_tecnico',
                  'problema_str', 'chamado_arquivado', 'estado', 'equipamento']
