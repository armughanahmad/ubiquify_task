from . import SQLAlchemyAutoSchema
from models.document_model import Document, db

class DocumentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        load_instance = True  # Optional: deserialize to model instances
        sqla_session = db.session
