from flask import Blueprint
from controllers.answer_controller import AnswerController

answer_bp = Blueprint('answer_bp', __name__)

@answer_bp.route('/api/answers', methods=['GET'])
def get_answers():
    return AnswerController.get_answers()

@answer_bp.route('/api/answers', methods=['POST'])
def add_answer():
    return AnswerController.add_answer()

@answer_bp.route('/api/answers/<int:answer_id>', methods=['GET'])
def get_answer(answer_id):
    return AnswerController.get_answer(answer_id)

@answer_bp.route('/api/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    return AnswerController.update_answer(answer_id)

@answer_bp.route('/api/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    return AnswerController.delete_answer(answer_id)
