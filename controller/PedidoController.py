import json
from server.appserver import server
from flask import Response, request
from service.PedidoService import PedidoService

app = server.app

service = PedidoService()


@app.route("/pedidos", methods=['GET'])
def get_pedidos():
    pedido = service.find_all()
    return json.dumps(pedido)
