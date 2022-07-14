import json
from flask import Flask, request
from dao.ClienteDAO import ClienteDAO
from flask import Response

app = Flask(__name__)

cliente = ClienteDAO()


@app.route("/clientes", methods=['GET'])
def get_cliente():
    return cliente.find_clientes()


@app.route("/cliente/<id>", methods=['GET'])
def get_cliente_id(id):
    return cliente.find_cliente(id)


@app.route("/cliente", methods=['POST'])
def create_cliente():
    cliente_request = request.get_json(force=True)
    cliente.create_cliente(cliente_request)
    return Response(None, status=201)


@app.route("/cliente", methods=['PUT'])
def update_cliente():
    cliente_request = request.get_json(force=True)
    cliente.update_cliente(cliente_request)
    return Response(None, status=201)


@app.route("/cliente/<id>", methods=['DELETE'])
def delete_cliente(id):
    return cliente.delete_cliente(id)


if __name__ == "__main__":
    app.run()
