from django.test import TestCase
from equipamentos.factories import (ChamadoEquipamentoFactory, EmpresaFactory,
                                    EquipamentoFactory, ProprietarioFactory,
                                    ResponsavelTecnicoFactory,
                                    TipoEquipamentoFactory)
from rest_framework.test import APIClient


class EmpresaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.empresas = EmpresaFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/empresa'

    def test_company_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_companies(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_api_shoud_delete_one_company(self):
        url = f'{self.url}/{self.empresas[1].id}'
        self.client.delete(url)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 4)

    def test_api_should_update_a_company(self):
        url = f'{self.url}/{self.empresas[0].id}'
        payload = {'nome': 'xablau'}
        self.client.put(url, payload)
        self.empresas[0].refresh_from_db()
        self.assertEqual(self.empresas[0].nome, 'xablau')


class ProprietarioTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.proprietarios = ProprietarioFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/proprietario'

    def test_proprietary_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_proprietaries(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_api_shoud_delete_one_company(self):
        url = f'{self.url}/{self.proprietarios[1].id}'
        self.client.delete(url)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 4)


class ProprietaryWithMaxEquipmentsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.proprietario1 = ProprietarioFactory(nome='Joao')
        cls.proprietario2 = ProprietarioFactory(nome='Paulo')
        EquipamentoFactory.create_batch(5, proprietario=cls.proprietario1)
        EquipamentoFactory.create_batch(2, proprietario=cls.proprietario2)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/proprietario/num_equipments'

    def test_proprietary_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_should_return_the_proprietary_with_max_num_of_equipments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['nome'], 'Joao')


class TipoEquipamentoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.tipo_equipamento = TipoEquipamentoFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/tipo_equipamento'

    def test_equipment_type_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_equipment_types(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_api_shoud_delete_one_equipment_type(self):
        url = f'{self.url}/{self.tipo_equipamento[1].id}'
        self.client.delete(url)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 4)

    def test_api_should_update_a_equipment_type(self):
        url = f'{self.url}/{self.tipo_equipamento[0].id}'
        payload = {'descricao': 'xablau'}
        self.client.put(url, payload)
        self.tipo_equipamento[0].refresh_from_db()
        self.assertEqual(self.tipo_equipamento[0].descricao, 'xablau')


class EquipamentoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.equipamento = EquipamentoFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/equipamento'

    def test_equipment_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_equipments(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_api_shoud_delete_one_equipment(self):
        url = f'{self.url}/{self.equipamento[1].id}'
        self.client.delete(url)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 4)


class EquipmentsWithMaxTicketsNumber(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.equipment1 = EquipamentoFactory(fabricante='Ark')
        cls.equipment2 = EquipamentoFactory(fabricante='Meds')
        ChamadoEquipamentoFactory.create_batch(5, equipamento=cls.equipment1)
        ChamadoEquipamentoFactory.create_batch(2, equipamento=cls.equipment2)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/equipamento/num_tickets'

    def test_equipment_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_should_return_equipment_with_max_num_of_tickets(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['fabricante'], 'Ark')


class ResponsavelTecnicoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.responsavel = ResponsavelTecnicoFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/responsavel_tecnico'

    def test_equipment_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_technical_managers(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_api_shoud_delete_one_echnical_manager(self):
        url = f'{self.url}/{self.responsavel[1].id}'
        self.client.delete(url)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 4)

    def test_api_should_update_a_echnical_manager(self):
        url = f'{self.url}/{self.responsavel[0].id}'
        payload = {'nome': 'xablau'}
        self.client.put(url, payload)
        self.responsavel[0].refresh_from_db()
        self.assertEqual(self.responsavel[0].nome, 'xablau')


class ChamadoEquipamentoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.chamados = ChamadoEquipamentoFactory.create_batch(5)

    def setUp(self):
        self.client = APIClient()
        self.url = '/equipamentos/chamado_equipamento'

    def test_tickett_api_should_return_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_api_should_return_five_tickets(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 5)

    def test_ticket_api_should_be_paginated(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.data['total_pages'], None)

    def test_ticket_api_should_return_max_100_items_per_page(self):
        ChamadoEquipamentoFactory.create_batch(200)
        response = self.client.get(self.url)
        self.assertGreater(response.data['total_pages'], 1)
        self.assertEqual(len(response.data['results']), 100)
