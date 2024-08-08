from flask import jsonify, request
from services.patent_application_service import PatentApplicationService
from schemas.patent_application_schema import PatentApplicationSchema

patent_application_schema = PatentApplicationSchema()
patent_applications_schema = PatentApplicationSchema(many=True)

class PatentApplicationController:
    @staticmethod
    def get_patent_applications():
        patent_applications = PatentApplicationService.get_all_patent_applications()
        result = patent_applications_schema.dump(patent_applications)
        return jsonify({"data":result})

    @staticmethod
    def add_patent_application():
        data = request.get_json()
        errors = patent_application_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        patent_application = PatentApplicationService.add_patent_application(data)
        result = patent_application_schema.dump(patent_application)
        return jsonify(result), 201

    @staticmethod
    def get_patent_application(patent_application_id):
        patent_application = PatentApplicationService.get_patent_application(patent_application_id)
        if patent_application is None:
            return jsonify({'message': 'PatentApplication not found'}), 404
        result = patent_application_schema.dump(patent_application)
        return jsonify(result)

    @staticmethod
    def update_patent_application(patent_application_id):
        data = request.get_json()
        errors = patent_application_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        patent_application = PatentApplicationService.update_patent_application(patent_application_id, data)
        if patent_application is None:
            return jsonify({'message': 'PatentApplication not found'}), 404
        result = patent_application_schema.dump(patent_application)
        return jsonify(result)

    @staticmethod
    def delete_patent_application(patent_application_id):
        patent_application = PatentApplicationService.get_patent_application(patent_application_id)
        if patent_application is None:
            return jsonify({'message': 'PatentApplication not found'}), 404
        patent_application = PatentApplicationService.delete_patent_application(patent_application_id)
        return {}, 204

    @staticmethod
    def submit_patent_application(patent_application_id):
        patent_application = PatentApplicationService.get_patent_application(patent_application_id)
        if patent_application is None:
            return jsonify({'message': 'PatentApplication not found'}), 404
        patent_application = PatentApplicationService.submit_patent_application(patent_application_id)
        return {}, 204
