from models.patent_application_model import PatentApplication, db

class PatentApplicationService:
    @staticmethod
    def get_all_patent_applications():
        return PatentApplication.query.all()

    @staticmethod
    def add_patent_application(data):
        new_patent_application = PatentApplication(**data)
        db.session.add(new_patent_application)
        db.session.commit()
        return new_patent_application

    @staticmethod
    def get_patent_application(patent_application_id):
        return PatentApplication.query.get(patent_application_id)

    @staticmethod
    def update_patent_application(patent_application_id, data):
        patent_application = PatentApplication.query.get(patent_application_id)
        if patent_application is None:
            return None
        for key, value in data.items():
            setattr(patent_application, key, value)
        db.session.commit()
        return patent_application

    @staticmethod
    def delete_patent_application(patent_application_id):
        patent_application = PatentApplication.query.get(patent_application_id)
        if patent_application is None:
            return False
        db.session.delete(patent_application)
        db.session.commit()
        return True

    @staticmethod
    def submit_patent_application(patent_application_id):
        patent_application = PatentApplication.query.get(patent_application_id)
        if patent_application is None:
            return False
        patent_application.status = 'submitted'
        db.session.commit()
        return True
