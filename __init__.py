from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
from app.authentication.models import * # importing models

app = None
def init_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.app_context().push()
    db.init_app(app)
    print('app has started......')
    return app
app = init_app() 

# db.create_all()

from app.home.controller import * # importing all controller

if __name__ == "__main__":
    app.run()

