"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:pass@127.0.0.1:3306/prayer_request'
app.config['SECRET_KEY'] = "LKJHOIHoih98y98"

db = SQLAlchemy(app)


import learningFlask.views