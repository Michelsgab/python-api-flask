import json
from models.Pedido import Pedido
from models.Cliente import Cliente
from models.Pagamento import Pagamento
from server.appserver import server
from flask import Response, request
from service.PagamentoService import PagamentoService

app = server.app

service = PagamentoService()


@app.route("/pagamentos", methods=['GET'])
def get_pagamentos():
    pagamento = service.find_all()
    return json.dumps(pagamento)


@app.route("/pagamento/<id>", methods=['GET'])
def get_id_pagamento(id):
    pagamento = service.find_by_id(id)
    return json.dumps(pagamento)


@app.route("/pagamento", methods=['POST'])
def post_pagamento():
    pagamento_request = request.get_json(force=True)
    cliente = Cliente(id=pagamento_request['pedido']['cliente']['id'],
                      nome=pagamento_request['pedido']['cliente']['nome'],
                      endereco=pagamento_request['pedido']['cliente']['endereco'],
                      telefone=pagamento_request['pedido']['cliente']['telefone'])
    pedido = Pedido(id=pagamento_request['pedido']['id'],
                    cliente=dict(cliente),
                    valor_total=pagamento_request['pedido']['valor_total'],
                    data_venda=pagamento_request['pedido']['data_venda'])
    pagamento = Pagamento(pedido=dict(pedido),
                          data_pagamento=pagamento_request['data_pagamento'])
    service.save(pagamento)
    return Response(None, status=201)


@app.route("/pagamento", methods=['PUT'])
def put_pagamento():
    pagamento_request = request.get_json(force=True)
    cliente = Cliente(id=pagamento_request['pedido']['cliente']['id'],
                      nome=pagamento_request['pedido']['cliente']['nome'],
                      endereco=pagamento_request['pedido']['cliente']['endereco'],
                      telefone=pagamento_request['pedido']['cliente']['telefone'])
    pedido = Pedido(id=pagamento_request['pedido']['id'],
                    cliente=dict(cliente),
                    valor_total=pagamento_request['pedido']['valor_total'],
                    data_venda=pagamento_request['pedido']['data_venda'])
    pagamento = Pagamento(id=pagamento_request['id'],
                          pedido=dict(pedido),
                          data_pagamento=pagamento_request['data_pagamento'])
    print(dict(pagamento))
    service.save(pagamento)
    return Response(None, status=201)


@app.route("/pagamento/<id>", methods=['DELETE'])
def delete_pagamento(id):
    service.delete(id)
    return Response(None, status=200)
