from . import db
from datetime import datetime, UTC

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    application_id = db.Column(db.Integer, db.ForeignKey('patent_application.id'), nullable=False)
