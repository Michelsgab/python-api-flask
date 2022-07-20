import logging
from models.Item import Item
from dao.factory.factory import getData
from service.ProdutoService import ProdutoService


class ItemDAO():
    def __init__(self):
        self._con = None
        try:
            connection = getData()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_itens(self, id_pedido):
        sql_command = f"""SELECT loja.db_loja.itens_pedido.id,
        loja.db_loja.itens_pedido.id_produto AS id_produto,
        loja.db_loja.itens_pedido.id_pedido  AS id_pedido,
        loja.db_loja.itens_pedido.quantidade, loja.db_loja.itens_pedido.valor
        FROM loja.db_loja.itens_pedido 
        WHERE loja.db_loja.itens_pedido.id_pedido = {id_pedido}"""
        cursor = self._con.cursor()

        try:
            logging.info("Método find_itens inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            item = Item()
            while row:
                produtoservice = ProdutoService()
                item.id = row[0]
                item.produto = produtoservice.find_by_id(row.id_produto)
                item.pedido = row[2]
                item.quantidade = row[3]
                item.valor = row[4]
                row = cursor.fetchone()

            return dict(item)
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_itens finalizado")
            cursor.close()

