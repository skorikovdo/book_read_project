from flask import Flask, request, Response
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_json('../config.json')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models