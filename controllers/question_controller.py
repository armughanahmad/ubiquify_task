from flask import jsonify, request
from services.question_service import QuestionService
from services.form_service import FormService
from schemas.question_schema import QuestionSchema

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)

class QuestionController:
    @staticmethod
    def get_questions():
        questions = QuestionService.get_all_questions()
        result = questions_schema.dump(questions)
        return jsonify({"data":result})

    @staticmethod
    def add_question():
        data = request.get_json()

        errors = question_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        # Enforcing Valid Form ID
        form_id = data['form_id']
        form = FormService.get_form(form_id)

        if not form:
            return jsonify({'message': 'Form not found'}), 404
        question = QuestionService.add_question(data)
        result = question_schema.dump(question)
        return jsonify(result), 201

    @staticmethod
    def get_question(question_id):
        question = QuestionService.get_question(question_id)
        if question is None:
            return jsonify({'message': 'Question not found'}), 404
        result = question_schema.dump(question)
        return jsonify(result)

    @staticmethod
    def update_question(question_id):
        data = request.get_json()
        errors = question_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        # Enforce Form ID
        form_id = data['form_id']
        form = FormService.get_form(form_id)

        if not form:
            return jsonify({'message': 'Form not found'}), 404
        question = QuestionService.update_question(question_id, data)
        if question is None:
            return jsonify({'message': 'Question not found'}), 404
        result = question_schema.dump(question)
        return jsonify(result)

    @staticmethod
    def delete_question(question_id):
        question = QuestionService.get_question(question_id)
        if question is None:
            return jsonify({'message': 'Question not found'}), 404
        question = QuestionService.delete_question(question_id)
        return {}, 204
