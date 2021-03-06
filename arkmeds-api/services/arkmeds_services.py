import requests


class Services:
    BASE_ENDPOINT = 'https://desenvolvimento.arkmeds.com'

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.payload = {
            "email": self.user,
            "password": self.password
        }
        self.token = self._get_token()

    def _get_token(self):
        try:
            return requests.request('POST',
                                    f'{self.BASE_ENDPOINT}/rest-auth/token-auth/',
                                    data=self.payload).json()['token']
        except Exception:
            return None

    def _make_requests(self, endpoint, method, data=None):
        error = False
        res = None
        headers = {
            'Authorization': f'JWT {self.token}',
        }
        try:
            res = requests.request(
                method, endpoint, headers=headers, data=data, timeout=5)
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            error = True
            info = {'error': error, 'message': err.__str__()}
            return error, info, res
        except requests.exceptions.ConnectionError as err:
            error = True
            info = {'error': error, 'message': err.__str__()}
            return error, info, res
        except requests.exceptions.Timeout as err:
            error = True
            info = {'error': error, 'message': err.__str__()}
            return error, info, res
        except requests.exceptions.RequestException as err:
            error = True
            info = {'error': error, 'message': err.__str__()}
            return error, info, res
        return False, {'error': error, 'message': 'Success'}, res

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
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v1/chamado/novo/', 'POST', data=data)

    def listar_empresas(self):
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v2/empresa/', 'GET')

    def empresa_detalhada(self, id):
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v2/company/{id}/', 'GET')

    def equipamentos_por_empresas(self, id, page=1):
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v2/equipamentos_paginados/?empresa_id={id}&page={page}', 'GET')

    def chamado_por_equipamento(self, id, page=1):
        return self._make_requests(f'{self.BASE_ENDPOINT}/api/v2/chamado/?equipamento_id={id}&page={page}', 'GET')
