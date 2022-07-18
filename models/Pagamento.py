class Pagamento():
    def __init__(self, id=None, pedido=None, data_pagamento=None):
        self._id = id
        self._pedido = pedido
        self._data_pagamento = data_pagamento

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def pedido(self):
        return self._pedido

    @pedido.setter
    def pedido(self, pedido):
        self._pedido = pedido

    @property
    def data_pagamento(self):
        return self._data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento):
        self._data_pagamento = data_pagamento

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)
