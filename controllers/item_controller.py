from flask import jsonify, request
from services.item_service import ItemService
from schemas.item_schema import ItemSchema

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class ItemController:
    @staticmethod
    def get_items():
        items = ItemService.get_all_items()
        result = items_schema.dump(items)
        return jsonify({"data":result})

    @staticmethod
    def add_item():
        data = request.get_json()
        errors = item_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        item = ItemService.add_item(data)
        result = item_schema.dump(item)
        return jsonify(result), 201

    @staticmethod
    def get_item(item_id):
        item = ItemService.get_item(item_id)
        if item is None:
            return jsonify({'message': 'Item not found'}), 404
        result = item_schema.dump(item)
        return jsonify(result)

    @staticmethod
    def update_item(item_id):
        data = request.get_json()
        errors = item_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        item = ItemService.update_item(item_id, data)
        if item is None:
            return jsonify({'message': 'Item not found'}), 404
        result = item_schema.dump(item)
