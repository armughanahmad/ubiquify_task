from . import SQLAlchemyAutoSchema
from models.question_model import Question, db

class QuestionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        load_instance = True  # Optional: deserialize to model instances
        sqla_session = db.session
        include_fk = True

    
