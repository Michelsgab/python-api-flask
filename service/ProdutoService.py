from flask import Response, request
from dao.ProdutoDAO import ProdutoDAO


class ProdutoService:

    def __init__(self):
        self.produto = ProdutoDAO()

    def find_all(self):
        return self.produto.find_produtos()

    def find_by_id(self, id):
        return self.produto.find_produto(id)

    def save(self, produto_request):
        produto_request = request.get_json(force=True)
        self.produto.create_produto(produto_request)
        return Response(None, status=201)

    def update(self, produto_request):
        produto_request = request.get_json(force=True)
        self.produto.update_produto(produto_request)
        return Response(None, status=200)

    def delete(self, id):
        return self.produto.delete_produto(id)
