from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .document_model import Document
from .patent_application_model import PatentApplication
from .answer_model import Answer
from .form_model import Form
from .question_model import Question