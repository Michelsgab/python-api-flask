import json
from server.appserver import server
from flask import Response, request, make_response
from service.ProdutoService import ProdutoService

app = server.app

service = ProdutoService()


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response({'erro': 'Não encontrado'}, 404)


@app.errorhandler(405)
def handle_405_error(_error):
    return make_response({'erro': 'Método não suportado pela URL'}, 405)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response({'erro': 'Houve um erro na aplicação'}, 500)


@app.route("/produtos", methods=['GET'])
def get_produtos():
    produto = service.find_all()
    return json.dumps(produto)


@app.route("/produto/<id>", methods=["GET"])
def get_id_produto(id):
    produto = service.find_by_id(id)
    return json.dumps(produto)


@app.route("/produto", methods=["POST"])
def post_produto():
    produto_request = request.get_json(force=True)
    service.save(produto_request)
    return Response(None, status=201)


@app.route("/produto", methods=['PUT'])
def put_produto():
    produto_request = request.get_json(force=True)
    service.update(produto_request)
    return Response(None, 200)


@app.route("/produto/<id>", methods=['DELETE'])
def delete_produto(id):
    return service.delete(id)
