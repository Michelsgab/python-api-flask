from dao.ItemDAO import ItemDAO


class ItemService:
    def __init__(self):
        self.item = ItemDAO()

    def find_by_id(self, id):
        return self.item.find_item(id)
