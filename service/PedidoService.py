from flask import Response, request
from dao.PedidoDAO import PedidoDAO


class PedidoService:
    def __init__(self):
        self.pedido = PedidoDAO()

    def find_all(self):
        return self.pedido.find_pedidos()

    def find_by_id(self, id):
        return self.pedido.find_pedido(id)

    def save(self, pedido_request):
        pedido_request = request.get_json(force=True)
        self.pedido.create_pedido(pedido_request)
        return Response(None, status=201)
