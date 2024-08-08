from models.form_model import Form, db

class FormService:
    @staticmethod
    def get_all_forms():
        return Form.query.all()

    @staticmethod
    def add_form(data):
        new_form = Form(**data)
        db.session.add(new_form)
        db.session.commit()
        return new_form

    @staticmethod
    def get_form(form_id):
        return Form.query.get(form_id)

    @staticmethod
    def update_form(form_id, data):
        form = Form.query.get(form_id)
        if form is None:
            return None
        for key, value in data.items():
            setattr(form, key, value)
        db.session.commit()
        return form

    @staticmethod
    def delete_form(form_id):
        form = Form.query.get(form_id)
        if form is None:
            return False
        db.session.delete(form)
        db.session.commit()
        return True
