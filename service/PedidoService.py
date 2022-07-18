from flask import Response, request
from dao.PedidoDAO import PedidoDAO


class PedidoService:
    def __init__(self):
        self.pedido = PedidoDAO()

    def find_all(self):
        return self.pedido.find_pedidos()
