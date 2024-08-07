from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.item_routes import item_bp
from models.item_model import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # or your preferred database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(item_bp)

if __name__ == "__main__":
    app.run(debug=True)
