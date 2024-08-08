from flask import Blueprint
from controllers.question_controller import QuestionController

question_bp = Blueprint('question_bp', __name__)

@question_bp.route('/api/questions', methods=['GET'])
def get_questions():
    return QuestionController.get_questions()

@question_bp.route('/api/questions', methods=['POST'])
def add_question():
    return QuestionController.add_question()

@question_bp.route('/api/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return QuestionController.get_question(question_id)

@question_bp.route('/api/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    return QuestionController.update_question(question_id)

@question_bp.route('/api/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return QuestionController.delete_question(question_id)
