from . import SQLAlchemyAutoSchema
from models.patent_application_model import PatentApplication, db

class PatentApplicationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PatentApplication
        load_instance = True  # Optional: deserialize to model instances
        sqla_session = db.session
