import requests


class Services:
    error = []
    BASE_ENDPOINT = 'https://desenvolvimento.arkmeds.com'

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.payload = {
            "email": self.user,
            "password": self.password
        }
        self.token = self.make_request(
            f'{self.BASE_ENDPOINT}/rest-auth/token-auth/',
            'POST',
            data=self.payload)

    def _make_requests(self, endpoint, method, data=None):
        headers = {
            'Authorization': f'JWT {self.token}',
        }
        response = None
        try:
            response = requests.request(
                method, endpoint, headers=headers, data=data, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err
        except requests.exceptions.ConnectionError as err:
            return err
        except requests.exceptions.Timeout as err:
            return err
        except requests.exceptions.RequestException as err:
            return err
        return response

    def criar_chamado(self,
                      equipamento,
                      solicitante,
                      tipo_servico,
                      problema,
                      observacoes,
                      data_criacao,
                      id_tipo_ordem_servico):
        data = {
            "equipamento": equipamento,
            "solicitante": solicitante,
            "tipo_servico": tipo_servico,
            "problema": problema,
            "observacoes": observacoes,
            "data_criacao": data_criacao,
            "id_tipo_ordem_servico": id_tipo_ordem_servico
        }
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v1/chamado/novo/',
                                   'POST',
                                   data=data).json()

    def listar_empresas(self):
        return self._make_requests(
            f'{self.BASE_ENDPOINT}/api/v2/empresa/', 'GET').json()

    def empresa_detalhada(self, id):
        return self._make_requests(
            f'{self.BASE_ENDPOINT}/api/v2/company/{id}/',
            'GET').json()

    def equipamentos_por_empresas(self, id):
        return self._make_requests(
            f'{self.BASE_ENDPOINT}/api/v2/equipamentos_paginados/?empresa_id={id}',
            'GET').json()

    def chamado_por_equipamento(self, id):
        return self._make_requests(
            f'{self.BASE_ENDPOINT}/api/v2/chamado/?equipamento_id={id}',
            'GET').json()
