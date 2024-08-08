from flask import Blueprint
from controllers.form_controller import FormController

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/api/forms', methods=['GET'])
def get_forms():
    return FormController.get_forms()

@form_bp.route('/api/forms', methods=['POST'])
def add_form():
    return FormController.add_form()

@form_bp.route('/api/forms/<int:form_id>', methods=['GET'])
def get_form(form_id):
    return FormController.get_form(form_id)

@form_bp.route('/api/forms/<int:form_id>', methods=['PUT'])
def update_form(form_id):
    return FormController.update_form(form_id)

@form_bp.route('/api/forms/<int:form_id>', methods=['DELETE'])
def delete_form(form_id):
    return FormController.delete_form(form_id)
