from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.secret_key = config.key
app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_data
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
