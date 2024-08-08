from flask import Blueprint
from controllers.document_controller import DocumentController

document_bp = Blueprint('document_bp', __name__)

@document_bp.route('/api/documents', methods=['GET'])
def get_documents():
    return DocumentController.get_documents()

@document_bp.route('/api/documents', methods=['POST'])
def add_document():
    return DocumentController.add_document()

@document_bp.route('/api/documents/<int:document_id>', methods=['GET'])
def get_document(document_id):
    return DocumentController.get_document(document_id)

@document_bp.route('/api/documents/<int:document_id>', methods=['PUT'])
def update_document(document_id):
    return DocumentController.update_document(document_id)

@document_bp.route('/api/documents/<int:document_id>', methods=['DELETE'])
def delete_document(document_id):
    return DocumentController.delete_document(document_id)
