import logging
from dao.factory.factory import getData
from models.Cliente import Cliente


class ClienteDAO():
    def __init__(self):
        self._con = None
        try:
            connection = getData()
            self._con = connection.get_connections()
        except Exception as err:
            raise err

    def find_clientes(self):
        lista_cliente = []
        sql_command = "SELECT * FROM loja.db_loja.cliente"
        cursor = self._con.cursor()
        try:
            logging.info("Método find_clientes inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            while row:
                cliente = Cliente()
                cliente.id = row[0]
                cliente.nome = row[1]
                cliente.endereco = row[2]
                cliente.telefone = row[3]
                lista_cliente.append(cliente)
                row = cursor.fetchone()
            lista_cliente_dict = []
            for cliente in lista_cliente:
                lista_cliente_dict.append(dict(cliente))

            return lista_cliente_dict
        except Exception as err:
            raise err
        finally:
            logging.info("Método find_clientes finalizado")
            cursor.close()

    def find_cliente(self, id):
        lista_cliente = []
        sql_command = f"SELECT * FROM loja.db_loja.cliente WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método find_cliente inicializado")
            cursor.execute(sql_command)
            row = cursor.fetchone()
            cliente = Cliente()
            while row:
                cliente.id = row[0]
                cliente.nome = row[1]
                cliente.endereco = row[2]
                cliente.telefone = row[3]
                lista_cliente.append(cliente)
                row = cursor.fetchone()

            return dict(cliente)

        except Exception as err:
            raise err
        finally:
            logging.info("Método find_cliente finalizado")
            cursor.close()

    def create_cliente(self, cliente_request):
        sql_command = "INSERT INTO loja.db_loja.cliente VALUES (?, ?, ?)"
        cliente_json = cliente_request
        cliente = Cliente(**cliente_json)
        cursor = self._con.cursor()
        try:
            logging.info("Método create_cliente inicializado")
            cursor.execute(sql_command, cliente.nome, cliente.endereco, cliente.telefone)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método create_cliente finalizado")
            cursor.close()

    def update_cliente(self, cliente_request):
        sql_command = f"UPDATE loja.db_loja.cliente SET nome = ?, endereco = ?, telefone = ? WHERE id = ?"
        cliente_json = cliente_request
        cliente = Cliente(**cliente_json)
        cursor = self._con.cursor()
        try:
            logging.info("Método update_cliente inicializado")
            cursor.execute(sql_command, cliente.nome, cliente.endereco, cliente.telefone, cliente.id)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            logging.info("Método update_cliente finalizado")
            cursor.close()

    def delete_cliente(self, id):
        sql_command = f"DELETE FROM loja.db_loja.cliente WHERE id = {id}"
        cursor = self._con.cursor()
        try:
            logging.info("Método delete_cliente inicializado")
            cursor.execute(sql_command)
            self._con.commit()
            return f"Cliente do id {id} deletado"
        except Exception as err:
            raise err
        finally:
            logging.info("Método delete_cliente finalizado")
            cursor.close()
