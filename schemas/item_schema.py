from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.item_model import Item, db

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True  # Optional: deserialize to model instances
        sqla_session = db.session
