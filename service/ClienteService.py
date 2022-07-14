from flask import Response, request
from dao.ClienteDAO import ClienteDAO


class ClienteService:

    def __init__(self):
        self.cliente = ClienteDAO()

    def find_all(self):
        return self.cliente.find_clientes()

    def find_by_id(self, id):
        return self.cliente.find_cliente(id)

    def save(self, cliente_request):
        cliente_request = request.get_json(force=True)
        self.cliente.create_cliente(cliente_request)
        return Response(None, status=201)

    def update(self, cliente_request):
        cliente_request = request.get_json(force=True)
        self.cliente.update_cliente(cliente_request)
        return Response(None, status=200)

    def delete(self, id):
        return self.cliente.delete_cliente(id)
