import logging
from dao.factory.factory import getData
from models.Produto import Produto


class ProdutoDAO():
    def __init__(self):
        self._con = None
        try:
            connection = getData()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_produtos(self):
        lista_produtos = []
        sql_command = "SELECT * FROM db_exercise.db_loja.tb_produtos"
        cursor = self._con.cursor()
        try:
            logging.info("Método find_produtos inicializando")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                produto = Produto()
                produto.id = row[0]
                produto.descricao = row[1]
                produto.preco = row[2]
                lista_produtos.append(produto)
                row = cursor.fetchone()
            lista_produtos_dict = []
            for produto in lista_produtos:
                lista_produtos_dict.append(dict(produto))

            return lista_produtos_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_produtos finalizado")
            cursor.close()

    def find_produto(self, id):
        lista_produto = []
        sql_command = f"SELECT * FROM db_exercise.db_loja.tb_produtos WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método find_produto inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                produto = Produto()
                produto.id = row[0]
                produto.descricao = row[1]
                produto.preco = row[2]
                lista_produto.append(produto)
                row = cursor.fetchone()
            lista_produto_dict = []
            for produto in lista_produto:
                lista_produto_dict.append(dict(produto))

            return lista_produto_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_produto finalizado")
            cursor.close()

    def create_produto(self, produto_request):
        sql_command = "INSERT INTO db_exercise.db_loja.tb_produtos VALUES (?, ?, ?)"
        produto_json = produto_request
        produto = Produto(**produto_json)
        cursor = self._con.cursor()
        try:
            logging.info("Método create_produto inicializado")
            cursor.execute(sql_command, produto.id, produto.descricao, produto.preco)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("étodo create_produto finalizado")
            cursor.close()

    def update_produto(self, produto_request):
        sql_command = f"UPDATE db_exercise.db_loja.tb_produtos SET descricao = ?, preco = ? WHERE id = ?"
        produto_json = produto_request
        produto = Produto(**produto_json)
        cursor = self._con.cursor()
        try:
            logging.info("Método update_produto inicializado")
            cursor.execute(sql_command, produto.descricao, produto.preco, produto.id)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método update_produto finalizado")
            cursor.close()

    def delete_produto(self, id):
        sql_command = f"DELETE FROM db_exercise.db_loja.tb_produtos = WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método delete_produto inicializado")
            cursor.execute(sql_command)
            self._con.commit()
            return f"Produto do id {id} deletado"
        except Exception as err:
            raise err
        finally:
            logging.info("Método delete_produto finalizado")
            cursor.close()
