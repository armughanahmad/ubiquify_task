from . import db
from datetime import datetime, UTC

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey('form.id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    keyname = db.Column(db.String(100), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    answers = db.relationship('Answer', backref='question', lazy=True)
    question_type = db.Column(db.String(50))
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    page = db.Column(db.Integer, nullable=False)


