import factory

from equipamentos.models import (Empresa, Equipamento, Proprietario,
                                 ResponsavelTecnico, TipoEquipamento,
                                 ChamadoEquipamento)


class EmpresaFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    tipo = factory.Faker('random_int', min=1, max=10)
    nome = factory.Sequence(lambda n: f'Nome {n + 1}')
    nome_fantasia = factory.Sequence(lambda n: f'Nome Fantasia {n + 1}')
    superior = factory.Sequence(lambda n: f'Superior {n + 1}')
    cnpj = '12345678912333333'
    observacoes = factory.Faker('sentence')
    contato = factory.Faker('sentence')
    email = 'teste@teste.com'
    telefone1 = '319999-9999'
    telefone2 = '319999-9999'
    ramal1 = '319999-9999'
    ramal2 = '319999-9999'
    fax = '319999-9999'
    cep = '1111222'
    rua = factory.Sequence(lambda n: f'Rua {n + 1}')
    numero = factory.Faker('random_int', min=1, max=10)
    bairro = factory.Sequence(lambda n: f'Bairro {n + 1}')
    cidade = factory.Sequence(lambda n: f'Cidade {n + 1}')
    estado = 'MG'

    class Meta:
        model = Empresa


class ProprietarioFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    nome = factory.Sequence(lambda n: f'Nome {n + 1}')
    apelido = factory.Sequence(lambda n: f'Apelido {n + 1}')

    class Meta:
        model = Proprietario


class TipoEquipamentoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    descricao = factory.Sequence(lambda n: f'Descricao {n + 1}')

    class Meta:
        model = TipoEquipamento


class EquipamentoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    fabricante = factory.Sequence(lambda n: f'Fabricante {n + 1}')
    modelo = factory.Sequence(lambda n: f'Modelo {n + 1}')
    patrimonio = factory.Sequence(lambda n: f'Patrimonion{n + 1}')
    numero_serie = '18273618273'
    identificacao = factory.Sequence(lambda n: f'Identificacao{n + 1}')
    proprietario = factory.SubFactory(ProprietarioFactory)
    tipo = factory.SubFactory(TipoEquipamentoFactory)
    qr_code = factory.Faker('random_int', min=-1, max=1)


    class Meta:
        model = Equipamento


class ResponsavelTecnicoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    has_avatar = factory.Faker('pybool')
    nome = factory.Sequence(lambda n: f'Nome {n + 1}')
    email = factory.Sequence(lambda n: f'email{n + 1}@teste.com')
    has_resp_tecnico = factory.Faker('pybool')
    avatar = factory.Sequence(lambda n: f'Avatar {n + 1}')

    class Meta:
        model = ResponsavelTecnico


class ChamadoEquipamentoFactory(factory.django.DjangoModelFactory):
    id = factory.Faker('random_int', min=1, max=99999999)
    chamados = factory.Faker('random_int', min=1, max=90)
    cor_prioridade = factory.Sequence(lambda n: f'#{n + 1}234')
    get_prioridade = factory.Sequence(lambda n: f'Prioridade {n + 1}')
    numero = factory.Faker('random_int', min=11111, max=99999)
    get_solicitante = factory.Sequence(lambda n: f'Solicitante {n + 1}')
    get_equipamento_servico = factory.Sequence(lambda n: f'Equipamento servico {n + 1}')
    get_criticidde = factory.Sequence(lambda n: f'Criticidade {n + 1}')
    tempo = []
    tempo_fechamento = []
    responsavel_str = factory.Sequence(lambda n: f'Responsavel {n + 1}')
    get_resp_tecnico = factory.SubFactory(ResponsavelTecnicoFactory)
    problema_str = factory.Sequence(lambda n: f'Problema {n + 1}')
    chamado_arquivado = factory.Faker('pybool')
    estado = factory.Faker('random_int', min=1, max=99999)
    equipamento = factory.SubFactory(EquipamentoFactory)

    class Meta:
        model = ChamadoEquipamento
