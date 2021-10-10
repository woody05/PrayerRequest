"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://sa:pass@192.168.200.68:3306/prayer_request'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:pass@localhost:3306/prayer_request'
app.config['SECRET_KEY'] = "LKJHOIHoih98y98"

app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
#lm = LoginManager(app)

import learningFlask.views