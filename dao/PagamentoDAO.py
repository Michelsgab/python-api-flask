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
        loja.db_loja.pagamento.id, loja.db_loja.pagamento.id_pedido_venda,
        loja.db_loja.pagamento.data_pagamento,
        pedido.id AS id_pedido FROM loja.db_loja.pagamento
        INNER JOIN loja.db_loja.pedido_venda pedido
        ON loja.db_loja.pagamento.id_pedido_venda = pedido.id"""
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
            lista_pagamento_dict = []
            for pagamento in lista_pagamento:
                lista_pagamento_dict.append(dict(pagamento))

            return lista_pagamento_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_pagamento finalizado")
            cursor.close()

    def find_pagamento(self, id):
        lista_pagamento = []
        sql_command = f"""SELECT
        loja.db_loja.pagamento.id, loja.db_loja.pagamento.id_pedido_venda,
        loja.db_loja.pagamento.data_pagamento,
        pedido.id  AS id_pedido FROM loja.db_loja.pagamento
        INNER JOIN loja.db_loja.pedido_venda pedido
        ON loja.db_loja.pagamento.id_pedido_venda = pedido.id
        WHERE loja.db_loja.pagamento.id = {id}"""
        cursor = self._con.cursor()

        try:
            logging.info("Método find_pagamento inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            pagamento = Pagamento()
            while row:
                pedidoservice = PedidoService()
                pagamento.id = row[0]
                pagamento.pedido = pedidoservice.find_by_id(row.id_pedido)
                pagamento.data_pagamento = str(row.data_pagamento)
                lista_pagamento.append(pagamento)
                row = cursor.fetchone()

            return dict(pagamento)
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_pagamento finalizado")
            cursor.close()

    def create_pagamento(self, pagamento):
        sql_command = "INSERT INTO loja.db_loja.pagamento OUTPUT Inserted.id VALUES (?, ?)"
        cursor = self._con.cursor()
        try:
            logging.info("Método create_pagamento inicializado")
            cursor.execute(sql_command, pagamento.pedido['id'], pagamento.data_pagamento)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método create_pagamento finalizado")
            cursor.close()

    def uptade_pagamento(self, pagamento):
        sql_command = "UPDATE loja.db_loja.pagamento SET id_pedido_venda = ?, data_pagamento = ? WHERE id = ?"
        cursor = self._con.cursor()
        try:
            logging.info("Método update_pagamento inicializado")
            cursor.execute(sql_command, pagamento.pedido['id'], pagamento.data_pagamento, pagamento.id)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método update_pagamento finalizado")
            cursor.close()

    def delete_pagamento(self, id):
        sql_command = f"DELETE from loja.db_loja.pagamento WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método delete_pagamento inicializado")
            cursor.execute(sql_command)
            self._con.commit()
            return f"Pagamento do id {id} deletado"
        except Exception as err:
            raise err
        finally:
            logging.info("Método delete_pagamento finalizado")
            cursor.close()

