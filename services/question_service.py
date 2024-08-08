from models.question_model import Question, db

class QuestionService:
    @staticmethod
    def get_all_questions():
        return Question.query.all()

    @staticmethod
    def add_question(data):
        new_question = Question(**data)
        db.session.add(new_question)
        db.session.commit()
        return new_question

    @staticmethod
    def get_question(question_id):
        return Question.query.get(question_id)

    @staticmethod
    def update_question(question_id, data):
        question = Question.query.get(question_id)
        if question is None:
            return None
        for key, value in data.items():
            setattr(question, key, value)
        db.session.commit()
        return question

    @staticmethod
    def delete_question(question_id):
        question = Question.query.get(question_id)
        if question is None:
            return False
        db.session.delete(question)
        db.session.commit()
        return True
