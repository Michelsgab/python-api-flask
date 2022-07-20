import logging
from service.ClienteService import ClienteService
from service.ItemService import ItemService
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
        loja.db_loja.pedido_venda.id, loja.db_loja.pedido_venda.id_cliente,
        loja.db_loja.pedido_venda.valor_total, loja.db_loja.pedido_venda.data_venda, 
        cliente.id AS id_cliente FROM loja.db_loja.pedido_venda
        INNER JOIN loja.db_loja.cliente cliente
        ON loja.db_loja.pedido_venda.id_cliente = cliente.id"""
        cursor = self._con.cursor()

        try:
            logging.info("Método find_pedidos inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                pedido = Pedido()
                clienteservice = ClienteService()
                itemservice = ItemService()
                pedido.id = row[0]
                pedido.cliente = clienteservice.find_by_id(row.id_cliente)
                pedido.itens = itemservice.find_all(row[0])
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

    def find_pedido(self, id):
        sql_command = f"""SELECT
        loja.db_loja.pedido_venda.id, loja.db_loja.pedido_venda.id_cliente,
        loja.db_loja.pedido_venda.valor_total, loja.db_loja.pedido_venda.data_venda, 
        cliente.id AS id_cliente FROM loja.db_loja.pedido_venda
        INNER JOIN loja.db_loja.cliente cliente
        ON loja.db_loja.pedido_venda.id_cliente = cliente.id
        WHERE loja.db_loja.pedido_venda.id = {id}"""
        cursor = self._con.cursor()
        try:
            logging.info("Método find_pedido inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            pedido = Pedido()
            while row:
                clienteservice = ClienteService()
                itemservice = ItemService()
                pedido.id = row[0]
                pedido.cliente = clienteservice.find_by_id(row.id_cliente)
                pedido.itens = itemservice.find_all(row[0])
                pedido.valor_total = int(row[2])
                pedido.data_venda = str(row[3])
                row = cursor.fetchone()

            return dict(pedido)

        except Exception as err:
            raise err
        finally:
            logging.info("Método find_pedido finalizado")
            cursor.close()

    def create_pedido(self, pedido):
        sql_command = "INSERT INTO loja.db_loja.pedido_venda OUTPUT Inserted.id VALUES (?, ?, ?)"
        cursor = self._con.cursor()
        try:
            logging.info("Método create_pedido inicializado")
            cursor.execute(sql_command, pedido.cliente['id'], pedido.valor_total, pedido.data_venda)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método create_pedido finalizado")
            cursor.close()

    def update_pedido(self, pedido):
        sql_command = "UPDATE loja.db_loja.pedido_venda SET id_cliente = ?, " \
                      "valor_total = ?, data_venda = ? WHERE id = ?"
        cursor = self._con.cursor()
        try:
            logging.info("Método update_pedido finalizado")
            cursor.execute(sql_command, pedido.cliente['id'], pedido.valor_total, pedido.data_venda, pedido.id)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método update_pedido finalizado")
            cursor.close()

    def delete_pedido(self, id):
        sql_command = f"DELETE from loja.db_loja.pedido_venda WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método delete_pedido inicializado")
            cursor.execute(sql_command)
            self._con.commit()
            return f"Pedido do id {id} deletado"
        except Exception as err:
            raise err
        finally:
            logging.info("Método delete_pedido finalizado")
            cursor.close()
