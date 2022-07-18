import logging
from service.PedidoService import PedidoService
from dao.factory.factory import getData
from models.Pagamento import Pagamento


class PagamentoDAO():
    def __init__(self):
        self._con = None
        try:
            connection = getData()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_pagamentos(self):
        lista_pagamento = []
        sql_command = """SELECT
        db_exercise.db_loja.tb_pagamento.id, db_exercise.db_loja.tb_pagamento.id_pedidoFK,
        db_exercise.db_loja.tb_pagamento.data_pagamento,
        pedido.id  AS id_pedido FROM db_exercise.db_loja.tb_pagamento
        INNER JOIN db_exercise.db_loja.tb_pedido pedido
        ON db_exercise.db_loja.tb_pagamento.id_pedidoFK = pedido.id"""
        cursor = self._con.cursor()

        try:
            logging.info("Método find_pagamentos inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                pagamento = Pagamento()
                pedidoservice = PedidoService()
                pagamento.id = row[0]
                pagamento.pedido = pedidoservice.find_by_id(row.id_pedido)
                pagamento.data_pagamento = str(row.data_pagamento)
                lista_pagamento.append(pagamento)
                row = cursor.fetchone()
                print(pagamento.pedido)
            lista_pagamento_dict = []
            for pagamento in lista_pagamento:
                lista_pagamento_dict.append(dict(pagamento))

            return lista_pagamento_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_pagamento finalizado")
            cursor.close()
