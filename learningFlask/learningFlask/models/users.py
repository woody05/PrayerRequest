
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

Base = declarative_base()

class users(UserMixin, db.Model):
    user_id = db.Column('User_id', db.Integer, primary_key = True)
    user_name = db.Column("User_name", db.Text)
    email_address = db.Column("Email_address", db.Text)
    first_name = db.Column("First_name", db.Text)
    last_name = db.Column("Last_Name", db.Text)
    password = db.Column("Password", db.String(200))

    comments = relationship("comments", back_populates="users")

    def set_password(self, password):
       """Create hashed password."""
       self.password = generate_password_hash(
           password,
           method='sha256'
       )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

def checkUserAccountExist(email):
    exist = users.query.filter_by(email_address = email).first()
    if exist is None:
        return False;

def createUser(user):
    if checkUserAccountExist(user.email_address) == False:
        user.set_password(user.password)
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False
