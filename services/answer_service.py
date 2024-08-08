from models.answer_model import Answer, db

class AnswerService:
    @staticmethod
    def get_all_answers():
        return Answer.query.all()

    @staticmethod
    def add_answer(data):
        new_answer = Answer(**data)
        db.session.add(new_answer)
        db.session.commit()
        return new_answer

    @staticmethod
    def get_answer(answer_id):
        return Answer.query.get(answer_id)

    @staticmethod
    def update_answer(answer_id, data):
        answer = Answer.query.get(answer_id)
        if answer is None:
            return None
        for key, value in data.items():
            setattr(answer, key, value)
        db.session.commit()
        return answer

    @staticmethod
    def delete_answer(answer_id):
        answer = Answer.query.get(answer_id)
        if answer is None:
            return False
        db.session.delete(answer)
        db.session.commit()
        return True
