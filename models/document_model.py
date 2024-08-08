from . import db
from datetime import datetime, UTC

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    application_id = db.Column(db.Integer, db.ForeignKey('patent_application.id'), nullable=False)

    def __repr__(self):
        return f'<Patent Application {self.name}>'

