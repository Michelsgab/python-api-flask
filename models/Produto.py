class Produto():
    def __init__(self, id=None, descricao=None, preco=None):
        self._id = id
        self._descricao = descricao
        self._preco = preco

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)