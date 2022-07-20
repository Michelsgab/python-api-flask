from dao.ItemDAO import ItemDAO


class ItemService:
    def __init__(self):
        self.item = ItemDAO()

    def find_all(self, id_pedido):
        return self.item.find_itens(id_pedido)
