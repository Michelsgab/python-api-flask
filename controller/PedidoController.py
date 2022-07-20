import json
from models.Cliente import Cliente
from models.Pedido import Pedido
from server.appserver import server
from flask import Response, request
from service.PedidoService import PedidoService

app = server.app

service = PedidoService()


@app.route("/pedidos", methods=['GET'])
def get_pedidos():
    pedido = service.find_all()
    return json.dumps(pedido)


@app.route("/pedido/<id>", methods=['GET'])
def get_id_pedido(id):
    pedido = service.find_by_id(id)
    return json.dumps(pedido)


@app.route("/pedido", methods=['POST'])
def post_pedido():
    pedido_request = request.get_json(force=True)
    cliente = Cliente(id=pedido_request['cliente']['id'],
                      nome=pedido_request['cliente']['nome'],
                      endereco=pedido_request['cliente']['endereco'],
                      telefone=pedido_request['cliente']['telefone'])
    pedido = Pedido(cliente=dict(cliente),
                    valor_total=pedido_request['valor_total'],
                    data_venda=pedido_request['data_venda'])
    service.save(pedido)
    return Response(None, status=201)


@app.route("/pedido", methods=['PUT'])
def put_pedido():
    pedido_request = request.get_json(force=True)
    cliente = Cliente(id=pedido_request['cliente']['id'],
                      nome=pedido_request['cliente']['nome'],
                      endereco=pedido_request['cliente']['endereco'],
                      telefone=pedido_request['cliente']['telefone'])
    pedido = Pedido(id=pedido_request['id'],
                    cliente=dict(cliente),
                    valor_total=pedido_request['valor_total'],
                    data_venda=pedido_request['data_venda'])
    service.update(pedido)
    return Response(None, 200)


@app.route("/pedido/<id>", methods=['DELETE'])
def delete_pedido(id):
    service.delete(id)
    return Response(None, status=200)
