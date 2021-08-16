
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class users(db.Model):
    user_id = db.Column('User_id', db.Integer, primary_key = True)
    user_name = db.Column("User_name", db.Text)
    email_address = db.Column("Email_address", db.Text)
    first_name = db.Column("First_name", db.Text)
    last_name = db.Column("Last_Name", db.Text)

    comments = relationship("comments", back_populates="users")

