import json, jsonify
from server.appserver import server
from flask import Response, request, make_response
from service.ClienteService import ClienteService

app = server.app

service = ClienteService()


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response({'erro': 'Não encontrado'}, 404)


@app.errorhandler(405)
def handle_405_error(_error):
    return make_response({'erro': 'Método não suportado pela URL'}, 405)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response({'erro': 'Houve um erro na aplicação'}, 500)


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
    return Response("Cliente criado", status=201)


@app.route("/cliente", methods=['PUT'])
def put_cliente():
    cliente_request = request.get_json(force=True)
    service.update(cliente_request)
    return Response(None, status=200)


@app.route("/cliente/<id>", methods=['DELETE'])
def delete_cliente(id):
    service.delete(id)
    return Response("Cliente deletado", status=200)
