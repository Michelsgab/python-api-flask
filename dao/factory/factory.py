import pyodbc


class getData:
    cursor = (
        r"Driver={ODBC Driver 17 for SQL Server};"
        r"Server=localhost;"
        r"Database=db_exercise;"
        r"Trusted_Connection=yes;"
    )

    def __init__(self):
        self.__errors = None

    def get_connections(self):
        conn = None
        try:
            conn = pyodbc.connect(self.cursor)
        except Exception as err:
            self.__errors = err
        return conn

    def close_connections(self, connection):
        try:
            connection.close()
        except Exception as err:
            self.__errors += err

    def get_errors(self):
        return self.__errors
