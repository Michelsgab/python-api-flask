import json
from flask import Flask, Response, request
from service.ClienteService import ClienteService

app = Flask(__name__)

service = ClienteService()


@app.route("/clientes", methods=['GET'])
def get():
    cliente = service.find_all()
    return json.dumps(cliente)


@app.route("/cliente/<id>", methods=['GET'])
def get_id(id):
    cliente = service.find_by_id(id)
    return json.dumps(cliente)


@app.route("/cliente", methods=['POST'])
def post():
    cliente_request = request.get_json(force=True)
    service.save(cliente_request)
    return Response(None, status=201)


@app.route("/cliente", methods=['PUT'])
def put():
    cliente_request = request.get_json(force=True)
    service.update(cliente_request)
    return Response(None, status=200)


@app.route("/cliente/<id>", methods=['DELETE'])
def delete(id):
    return service.delete(id)
