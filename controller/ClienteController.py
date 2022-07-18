import json
from server.appserver import server
from flask import Response, request
from service.ClienteService import ClienteService

app = server.app

service = ClienteService()


@app.route("/clientes", methods=['GET'])
def get_clientes():
    cliente = service.find_all()
    return json.dumps(cliente)


@app.route("/cliente/<id>", methods=['GET'])
def get_id_cliente(id):
    cliente = service.find_by_id(id)
    return json.dumps(cliente)


@app.route("/cliente", methods=['POST'])
def post_cliente():
    cliente_request = request.get_json(force=True)
    service.save(cliente_request)
    return Response(None, status=201)


@app.route("/cliente", methods=['PUT'])
def put_cliente():
    cliente_request = request.get_json(force=True)
    service.update(cliente_request)
    return Response(None, status=200)


@app.route("/cliente/<id>", methods=['DELETE'])
def delete_cliente(id):
    return service.delete(id)
