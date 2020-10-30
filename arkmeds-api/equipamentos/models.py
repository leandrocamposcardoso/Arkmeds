from django.db import models


class Empresa(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)


class Detalhe(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    empresa = models.ForeignKey(
        'Empresa',
        models.PROTECT,
        blank=True,
        null=True,
        related_name='+')
    tipo = models.ForeignKey(
        'TipoDetalhe',
        models.PROTECT,
        blank=True,
        null=True,
    )
    nome = models.CharField(max_length=100, null=True)
    nome_fantasia = models.CharField(max_length=100, null=True)
    superior = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=20, null=True)
    observacoes = models.TextField(max_length=500, null=True)
    contato = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    telefone1 = models.CharField(max_length=20, null=True)
    ramal1 = models.CharField(max_length=20, null=True)
    telefone2 = models.CharField(max_length=20, null=True)
    ramal2 = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    cep = models.CharField(max_length=12, null=True)
    rua = models.CharField(max_length=100, null=True)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=2, null=True)


class TipoDetalhe(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)


class Equipamento(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patrimonio = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(
        'Proprietario',
        models.PROTECT,
        blank=True,
        null=True,
    )
    tipo = models.ForeignKey(
        'TipoEquipamento',
        models.PROTECT,
        blank=True,
        null=True,
    )
    qr_code = models.IntegerField()


class Proprietario(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)


class TipoEquipamento(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    descricao = models.TextField(max_length=500)


class Chamado(models.Model):
    equipamento = models.ForeignKey(
        'Equipamento',
        models.PROTECT,
        blank=True,
        null=True,
    )
    solicitante = models.ForeignKey(
        'Solicitante',
        models.PROTECT,
        blank=True,
        null=True,
    )
    tipo_servico = models.ForeignKey(
        'TipoServico',
        models.PROTECT,
        blank=True,
        null=True,
    )
    problema = models.ForeignKey(
        'Problema',
        models.PROTECT,
        blank=True,
        null=True,
    )
    observacoes = models.TextField()
    data_criacao = models.DateTimeField()
    id_tipo_ordem_servico = models.ForeignKey(
        'TipoOrdemServico',
        models.PROTECT,
        blank=True,
        null=True,
    )


class Solicitante(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)


class TipoServico(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)


class Problema(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)


class TipoOrdemServico(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)


class ChamadoEquipamento(models.Model):
    chamado = models.ForeignKey(
        'Chamado',
        models.PROTECT,
        blank=True,
        null=True,
    )
    cor_prioridade = models.CharField(max_length=100)
    prioridade = models.PositiveSmallIntegerField()
    get_prioridade = models.CharField(max_length=100)
    numero = models.IntegerField()
    get_solicitante = models.CharField(max_length=100)
    get_equipamento_servico = models.CharField(max_length=100)
    get_criticidde = models.CharField(max_length=100)
    get_criticidde = models.CharField(max_length=100)
