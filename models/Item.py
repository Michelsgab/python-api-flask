class Item:
    def __init__(self, id=None, produto=None, pedido=None, quantidade=None, valor=None):
        self._id = id
        self._produto = produto
        self._pedido = pedido
        self._quantidade = quantidade
        self._valor = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, produto):
        self._produto = produto

    @property
    def pedido(self):
        return self._pedido

    @pedido.setter
    def pedido(self, pedido):
        self._pedido = pedido

    @pedido.deleter
    def pedido(self):
        print(self._pedido, "foi deletado")
        del self._pedido

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)
