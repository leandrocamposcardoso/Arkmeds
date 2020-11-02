from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from equipamentos.models import (ChamadoEquipamento, Empresa, Equipamento,
                                 Proprietario, ResponsavelTecnico,
                                 TipoEquipamento)

from .serializers import (ChamadoEquipamentoSerializer, EmpresaSerializer,
                          EquipamentoSerializer, ProprietarioSerializer,
                          ResposavelTecnicoSerializer,
                          TipoEquipamentoSerializer)
from helpers.pagination import BigPagination


class EmpresaView(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()


class EquipamentoView(viewsets.ModelViewSet):
    serializer_class = EquipamentoSerializer
    queryset = Equipamento.objects.all()

    @action(detail=False, methods=['GET'])
    def num_tickets(self, request):
        equipamento = Equipamento.objects.select_related('tipo', 'proprietario').annotate(
            num_tickets=Count('chamadoequipamento')).order_by('-num_tickets').first()

        proprietario = {
            'id': equipamento.proprietario.id,
            'nome': equipamento.proprietario.nome,
            'apelido': equipamento.proprietario.apelido
        }
        tipo = {
            'id': equipamento.tipo.id,
            'descricao': equipamento.tipo.descricao
        }
        resp_data = {
            'id': equipamento.id,
            'fabricante': equipamento.fabricante,
            'modelo': equipamento.modelo,
            'patrimonio': equipamento.patrimonio,
            'identificacao': equipamento.identificacao,
            'proprietario': proprietario,
            'tipo': tipo,
            'qr_code': equipamento.qr_code,
            'quantidade_chamados': equipamento.num_tickets,
        }
        return Response(resp_data)


class ProprietarioView(viewsets.ModelViewSet):
    serializer_class = ProprietarioSerializer
    queryset = Proprietario.objects.all()

    @action(detail=False, methods=['GET'])
    def num_equipments(self, request):
        proprietario = Proprietario.objects.annotate(
            num_equipments=Count('equipamento')).order_by('-num_equipments').first()

        resp_data = {
            'id': proprietario.id,
            'nome': proprietario.nome,
            'quantidade_equipamentos': proprietario.num_equipments,
        }
        return Response(resp_data)


class TipoEquipamentoView(viewsets.ModelViewSet):
    serializer_class = TipoEquipamentoSerializer
    queryset = TipoEquipamento.objects.all()


class ResponsavelTecnicoView(viewsets.ModelViewSet):
    serializer_class = ResposavelTecnicoSerializer
    queryset = ResponsavelTecnico.objects.all()


class ChamadoEquipamentoView(viewsets.ModelViewSet):
    pagination_class = BigPagination
    serializer_class = ChamadoEquipamentoSerializer
    queryset = ChamadoEquipamento.objects.all()
