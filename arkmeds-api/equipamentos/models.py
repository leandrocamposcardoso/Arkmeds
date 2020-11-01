from django.db import models


class Empresa(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    tipo = models.PositiveIntegerField(null=True)
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

    def __str__(self):
        return self.nome


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

    def __str__(self):
        return self.modelo


class Proprietario(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class TipoEquipamento(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.descricao


class ResponsavelTecnico(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    has_avatar = models.BooleanField(default=False)
    nome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    has_resp_tecnico = models.BooleanField(default=False)
    avatar = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome


class ChamadoEquipamento(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    chamados = models.IntegerField(null=True)
    cor_prioridade = models.CharField(max_length=100, null=True)
    prioridade = models.PositiveSmallIntegerField(null=True)
    get_prioridade = models.CharField(max_length=100, null=True)
    numero = models.IntegerField()
    get_solicitante = models.CharField(max_length=100, null=True)
    get_equipamento_servico = models.CharField(max_length=100, null=True)
    get_criticidde = models.CharField(max_length=100)
    tempo = models.JSONField(null=True)
    tempo_fechamento = models.JSONField(null=True)
    responsavel_str = models.CharField(max_length=100, null=True)
    get_resp_tecnico = models.ForeignKey(
        'ResponsavelTecnico',
        models.PROTECT,
        blank=True,
        null=True,
    )
    problema_str = models.CharField(max_length=100, null=True)
    chamado_arquivado = models.BooleanField(default=False)
    estado = models.PositiveIntegerField(editable=False, null=True)
    equipamento = models.ForeignKey(
        'Equipamento',
        models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.chamados)
