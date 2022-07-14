import json
from flask import Flask, Response, request
from service.ProdutoService import ProdutoService

app = Flask(__name__)

service = ProdutoService()


@app.route("/produtos", methods=['GET'])
def get():
    produto = service.find_all()
    return json.dumps(produto)


@app.route("/produto/<id>", methods=["GET"])
def get_id(id):
    produto = service.find_by_id(id)
    return json.dumps(produto)


@app.route("/produto", methods=["POST"])
def post():
    produto_request = request.get_json(force=True)
    service.save(produto_request)
    return Response(None, status=201)


@app.route("/produto", methods=['PUT'])
def put():
    produto_request = request.get_json(force=True)
    service.update(produto_request)
    return Response(None, 200)


@app.route("/produto/<id>", methods=['DELETE'])
def delete(id):
    return service.delete(id)
