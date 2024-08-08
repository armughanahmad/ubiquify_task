from flask import jsonify, request
from services.form_service import FormService
from schemas.form_schema import FormSchema

form_schema = FormSchema()
forms_schema = FormSchema(many=True)

class FormController:
    @staticmethod
    def get_forms():
        forms = FormService.get_all_forms()
        result = forms_schema.dump(forms)
        return jsonify({"data":result})

    @staticmethod
    def add_form():
        data = request.get_json()
        errors = form_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        form = FormService.add_form(data)
        result = form_schema.dump(form)
        return jsonify(result), 201

    @staticmethod
    def get_form(form_id):
        form = FormService.get_form(form_id)
        if form is None:
            return jsonify({'message': 'Form not found'}), 404
        result = form_schema.dump(form)
        return jsonify(result)

    @staticmethod
    def update_form(form_id):
        data = request.get_json()
        errors = form_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        form = FormService.update_form(form_id, data)
        if form is None:
            return jsonify({'message': 'Form not found'}), 404
        result = form_schema.dump(form)
        return jsonify(result)

    @staticmethod
    def delete_form(form_id):
        form = FormService.get_form(form_id)
        if form is None:
            return jsonify({'message': 'Form not found'}), 404
        form = FormService.delete_form(form_id)
        return {}, 204
