from flask import jsonify, request
from services.answer_service import AnswerService
from schemas.answer_schema import AnswerSchema

answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)

class AnswerController:
    @staticmethod
    def get_answers():
        answers = AnswerService.get_all_answers()
        result = answers_schema.dump(answers)
        return jsonify({"data":result})

    @staticmethod
    def add_answer():
        data = request.get_json()
        errors = answer_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        answer = AnswerService.add_answer(data)
        result = answer_schema.dump(answer)
        return jsonify(result), 201

    @staticmethod
    def get_answer(answer_id):
        answer = AnswerService.get_answer(answer_id)
        if answer is None:
            return jsonify({'message': 'Answer not found'}), 404
        result = answer_schema.dump(answer)
        return jsonify(result)

    @staticmethod
    def update_answer(answer_id):
        data = request.get_json()
        errors = answer_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        answer = AnswerService.update_answer(answer_id, data)
        if answer is None:
            return jsonify({'message': 'Answer not found'}), 404
        result = answer_schema.dump(answer)
        return jsonify(result)

    @staticmethod
    def delete_answer(answer_id):
        answer = AnswerService.get_answer(answer_id)
        if answer is None:
            return jsonify({'message': 'Answer not found'}), 404
        answer = AnswerService.delete_answer(answer_id)
        return {}, 204
