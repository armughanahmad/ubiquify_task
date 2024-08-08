from . import db
from datetime import datetime, UTC

class PatentApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    documents = db.relationship('Document', backref='application', lazy=True, cascade='all, delete-orphan')
    answers = db.relationship('Answer', backref='patent_application', lazy=True, cascade='all, delete-orphan')
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __repr__(self):
        return f'<Patent Application {self.name}>'

