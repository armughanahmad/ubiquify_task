from flask import Blueprint
from controllers.item_controller import ItemController

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/api/items', methods=['GET'])
def get_items():
    return ItemController.get_items()

@item_bp.route('/api/items', methods=['POST'])
def add_item():
    return ItemController.add_item()

@item_bp.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return ItemController.get_item(item_id)

@item_bp.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return ItemController.update_item(item_id)

@item_bp.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return ItemController.delete_item(item_id)
