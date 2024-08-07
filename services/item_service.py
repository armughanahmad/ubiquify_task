from models.item_model import Item, db

class ItemService:
    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def add_item(data):
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def get_item(item_id):
        return Item.query.get(item_id)

    @staticmethod
    def update_item(item_id, data):
        item = Item.query.get(item_id)
        if item is None:
            return None
        item.name = data['name']
        db.session.commit()
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get(item_id)
        if item is None:
            return False
        db.session.delete(item)
        db.session.commit()
        return True
