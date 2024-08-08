from . import SQLAlchemyAutoSchema
from models.form_model import Form, db

class FormSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Form
        load_instance = True  # Optional: deserialize to model instances
        sqla_session = db.session
