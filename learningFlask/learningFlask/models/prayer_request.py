from learningFlask import app
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from . import comment,users
#from datatables import ColumnDT, DataTables

Base = declarative_base()

class prayer_request(db.Model):
    prayer_request_id = db.Column('Prayer_Request_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.Text, nullable=False)
    description = db.Column("Description",db.Text, nullable=False)
    is_answered = db.Column("IsAnswered", db.Integer, nullable=False)
    added_by = db.Column("Add_By",db.Text, nullable=False)
    date_added = db.Column("Date_Added",db.DateTime, nullable=False)
    date_answered = db.Column("Date_Answered",db.DateTime, nullable=False)
    
    category_id = db.Column("Category_id", db.Integer, ForeignKey("category.Category_id"))
    _category = relationship("category")

    comments = relationship("comments", back_populates="prayer_request")


def all_prayer_request():
    result = prayer_request.query
    return result

def unanswered_prayer_request():
    data = prayer_request.query.filter_by(is_answered=0)
    return data


def answered_prayer_request():
    data = prayer_request.query.filter_by(is_answered=1)
    return data


def prayer_request_by_id(id):
    result = prayer_request.query.filter_by(prayer_request_id=id).first()
    return result



def remove_prayer_request(id):
    result = prayer_request.query.filter_by(prayer_request_id=id).first()
    db.session.delete(result)
    db.session.commit()

def update_prayer_request(updatedData):
    result = prayer_request.query.filter_by(prayer_request_id=updatedData.prayer_request_id).first()
    result.description = updatedData.description
    result.added_by = updatedData.added_by
    result.date_added = updatedData.date_added
    result.is_answered = updatedData.is_answered
    result.category_id = updatedData.category_id


    if updatedData.date_answered != None and updatedData.date_answered != '':
        result.date_answered = updatedData.date_answered

    print(result.prayer_request_id)
    print(result.description)
    print(result.added_by)
    print(result.date_added)

    db.session.commit()

def add_prayer_request(title,description,person,category_id):
   newRequest = prayer_request()
   newRequest.title = title
   newRequest.description = description
   newRequest.is_answered = 0
   newRequest.added_by = person
   newRequest.category_id = category_id
   newRequest.date_added = datetime.now()
   newRequest.date_answered = None

   db.session.add(newRequest)
   db.session.commit()

