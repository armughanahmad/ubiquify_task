from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.item_routes import item_bp
from routes.form_routes import form_bp
from routes.question_routes import question_bp
from routes.document_routes import document_bp
from routes.patent_application_routes import patent_application_bp
from routes.answer_routes import answer_bp  
from models import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # or your preferred database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(item_bp)
app.register_blueprint(form_bp)
app.register_blueprint(document_bp)
app.register_blueprint(patent_application_bp)
app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)

if __name__ == "__main__":
    app.run(debug=True)
