import json
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
        sql_command = "SELECT * FROM db_exercise.db_loja.tb_cliente"
        cursor = self._con.cursor()
        try:
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

            return json.dumps(lista_cliente_dict)
        except Exception as err:
            raise err
        finally:
            cursor.close()

    def find_cliente(self, id):
        lista_cliente = []
        sql_command = f"SELECT * FROM db_exercise.db_loja.tb_cliente WHERE id = {id}"
        cursor = self._con.cursor()
        try:
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

            return json.dumps(lista_cliente_dict)
        except Exception as err:
            raise err
        finally:
            cursor.close()

    def create_cliente(self, cliente_request):
        sql_command = "INSERT INTO db_exercise.db_loja.tb_cliente VALUES (?, ?, ?, ?)"
        cliente_json = cliente_request
        cliente = Cliente(**cliente_json)
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_command, cliente.id, cliente.nome, cliente.endereco, cliente.telefone)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            cursor.close()

    def update_cliente(self, cliente_request):
        sql_command = f"UPDATE db_exercise.db_loja.tb_cliente SET nome = ?, endereco = ?, telefone = ? WHERE id = ?"
        cliente_json = cliente_request
        cliente = Cliente(**cliente_json)
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_command, cliente.nome, cliente.endereco, cliente.telefone, cliente.id)
            self._con.commit()
        except Exception as err:
            raise err
        finally:
            cursor.close()

    def delete_cliente(self, id):
        sql_command = "DELETE FROM db_exercise.db_loja.tb_cliente WHERE id = " + id
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_command)
            self._con.commit()
            return "Cliente deletado"
        except Exception as err:
            raise err
        finally:
            cursor.close()
