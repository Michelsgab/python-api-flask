from flask import Response, request
from dao.PagamentoDAO import PagamentoDAO


class PagamentoService:
    def __init__(self):
        self.pagamento = PagamentoDAO()

    def find_all(self):
        return self.pagamento.find_pagamentos()

    def find_by_id(self, id):
        return self.pagamento.find_pagamento(id)

    def save(self, pagamento):
        self.pagamento.create_pagamento(pagamento)
        return Response(None, status=201)

    def update(self, pagamento):
        self.pagamento.uptade_pagamento(pagamento)
        return Response(None, status=200)

    def delete(self, id):
        self.pagamento.delete_pagamento(id)
        return Response(None, status=200)
