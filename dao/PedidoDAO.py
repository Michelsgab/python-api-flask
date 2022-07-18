import logging
from service.ClienteService import ClienteService
from dao.factory.factory import getData
from models.Pedido import Pedido


class PedidoDAO():
    def __init__(self):
        self._con = None
        try:
            connection = getData()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_pedidos(self):
        lista_pedido = []
        sql_command = """SELECT
        db_exercise.db_loja.tb_pedido.id, db_exercise.db_loja.tb_pedido.id_clienteFK,
        db_exercise.db_loja.tb_pedido.valor_total, db_exercise.db_loja.tb_pedido.data_venda, 
        cliente.id AS id_cliente FROM db_exercise.db_loja.tb_pedido
        INNER JOIN db_exercise.db_loja.tb_cliente cliente
        ON db_exercise.db_loja.tb_pedido.id_clienteFK = cliente.id"""
        cursor = self._con.cursor()

        try:
            logging.info("Método find_pedidos inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                pedido = Pedido()
                clienteservice = ClienteService()
                pedido.id = row[0]
                pedido.cliente = clienteservice.find_by_id(row.id_cliente)
                pedido.valor_total = int(row[2])
                pedido.data_venda = str(row[3])
                lista_pedido.append(pedido)
                row = cursor.fetchone()
            lista_pedido_dict = []
            for pedido in lista_pedido:
                lista_pedido_dict.append(dict(pedido))

            return lista_pedido_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_pedidos finalizado")
            cursor.close()
