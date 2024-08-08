from models.document_model import Document, db

class DocumentService:
    @staticmethod
    def get_all_documents():
        return Document.query.all()

    @staticmethod
    def add_document(data):
        new_document = Document(**data)
        db.session.add(new_document)
        db.session.commit()
        return new_document

    @staticmethod
    def get_document(document_id):
        return Document.query.get(document_id)

    @staticmethod
    def update_document(document_id, data):
        document = Document.query.get(document_id)
        if document is None:
            return None
        for key, value in data.items():
            setattr(document, key, value)
        db.session.commit()
        return document

    @staticmethod
    def delete_document(document_id):
        document = Document.query.get(document_id)
        if document is None:
            return False
        db.session.delete(document)
        db.session.commit()
        return True
