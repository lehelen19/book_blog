import os
from pickle import FALSE
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Flask-SQLAlchemy extension takes location of database, our base directory if url unprovided
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False