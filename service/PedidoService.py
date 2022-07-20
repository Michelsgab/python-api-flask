from flask import Response, request
from dao.PedidoDAO import PedidoDAO


class PedidoService:
    def __init__(self):
        self.pedido = PedidoDAO()

    def find_all(self):
        return self.pedido.find_pedidos()

    def find_by_id(self, id):
        return self.pedido.find_pedido(id)

    def save(self, pedido):
        self.pedido.create_pedido(pedido)
        return Response(None, status=201)

    def update(self, pedido):
        self.pedido.update_pedido(pedido)
        return Response(None, status=200)

    def delete(self, id):
        self.pedido.delete_pedido(id)
        return Response(None, status=200)
