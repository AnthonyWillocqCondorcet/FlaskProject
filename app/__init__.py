from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#clé secrète générée dans la console Python de Pycharm
app.config['SECRET_KEY'] = '81104011751ac9f2e6f46c45f2dfba32'
#supprime les notifications inutiles
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://anonyme:anonyme@host.docker.internal:5432/Brasserie"

db = SQLAlchemy(app)

from app import routes