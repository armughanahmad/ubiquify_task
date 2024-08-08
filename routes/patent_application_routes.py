from flask import Blueprint
from controllers.patent_application_controller import PatentApplicationController

patent_application_bp = Blueprint('patent_application_bp', __name__)

@patent_application_bp.route('/api/patent_applications', methods=['GET'])
def get_patent_applications():
    return PatentApplicationController.get_patent_applications()

@patent_application_bp.route('/api/patent_applications', methods=['POST'])
def add_patent_application():
    return PatentApplicationController.add_patent_application()

@patent_application_bp.route('/api/patent_applications/submit/<int:patent_application_id>', methods=['GET'])
def submit_patent_application():
    return PatentApplicationController.submit_patent_application()

@patent_application_bp.route('/api/patent_applications/<int:patent_application_id>', methods=['GET'])
def get_patent_application(patent_application_id):
    return PatentApplicationController.get_patent_application(patent_application_id)

@patent_application_bp.route('/api/patent_applications/<int:patent_application_id>', methods=['PUT'])
def update_patent_application(patent_application_id):
    return PatentApplicationController.update_patent_application(patent_application_id)

@patent_application_bp.route('/api/patent_applications/<int:patent_application_id>', methods=['DELETE'])
def delete_patent_application(patent_application_id):
    return PatentApplicationController.delete_patent_application(patent_application_id)
