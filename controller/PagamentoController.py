import json
from server.appserver import server
from service.PagamentoService import PagamentoService

app = server.app

service = PagamentoService()


@app.route("/pagamentos", methods=['GET'])
def get_pagamentos():
    pagamento = service.find_all()
    return json.dumps(pagamento)
