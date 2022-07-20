class Pedido():
    def __init__(self, id=None, cliente=None, itens=[], valor_total=None, data_venda=None):
        self._id = id
        self._cliente = cliente
        self._itens = itens
        self._valor_total = valor_total
        self._data_venda = data_venda

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, itens):
        self._itens = itens

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self._valor_total = valor_total

    @property
    def data_venda(self):
        return self._data_venda

    @data_venda.setter
    def data_venda(self, data_venda):
        self._data_venda = data_venda

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)
