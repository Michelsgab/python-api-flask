from flask import Response, request
from dao.PagamentoDAO import PagamentoDAO


class PagamentoService:
    def __init__(self):
        self.pagamento = PagamentoDAO()

    def find_all(self):
        return self.pagamento.find_pagamentos()
