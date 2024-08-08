from flask import jsonify, request
from services.document_service import DocumentService
from schemas.document_schema import DocumentSchema

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)

class DocumentController:
    @staticmethod
    def get_documents():
        documents = DocumentService.get_all_documents()
        result = documents_schema.dump(documents)
        return jsonify({"data":result})

    @staticmethod
    def add_document():
        data = request.get_json()
        errors = document_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        document = DocumentService.add_document(data)
        result = document_schema.dump(document)
        return jsonify(result), 201

    @staticmethod
    def get_document(document_id):
        document = DocumentService.get_document(document_id)
        if document is None:
            return jsonify({'message': 'Document not found'}), 404
        result = document_schema.dump(document)
        return jsonify(result)

    @staticmethod
    def update_document(document_id):
        data = request.get_json()
        errors = document_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        document = DocumentService.update_document(document_id, data)
        if document is None:
            return jsonify({'message': 'Document not found'}), 404
        result = document_schema.dump(document)
        return jsonify(result)

    @staticmethod
    def delete_document(document_id):
        document = DocumentService.get_document(document_id)
        if document is None:
            return jsonify({'message': 'Document not found'}), 404
        document = DocumentService.delete_document(document_id)
        return {}, 204
