from . import db
from datetime import datetime, UTC

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    questions = db.relationship('Question', backref='form', lazy=True)
    initial_question = db.Column(db.String(5000), nullable=True)
    end_question = db.Column(db.String(5000), nullable=True)
    document = db.Column(db.String(255))
    can_edit = db.Column(db.Boolean, default=True)

