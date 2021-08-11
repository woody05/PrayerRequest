from learningFlask import app
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from datatables import ColumnDT, DataTables

Base = declarative_base()

class prayer_request(db.Model):
    prayer_request_id = db.Column('Prayer_Request_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.Text, nullable=False)
    description = db.Column("Description",db.Text, nullable=False)
    is_answered = db.Column("IsAnswered", db.Integer, nullable=False)
    added_by = db.Column("Add_By",db.Text, nullable=False)
    date_added = db.Column("Date_Added",db.DateTime, nullable=False)
    date_answered = db.Column("Date_Answered",db.DateTime, nullable=False)
    category_id = db.Column("Category_id", db.Integer, nullable=False)

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


def unAnswered_prayer_request_datatables(request):
    data = unanswered_prayer_request()
    params = request.args

    columns = []
    columns.append(ColumnDT(prayer_request.title))
    #columns.append(ColumnDT(text("prayer_request.description")))
    #columns.append(ColumnDT(text('prayer_request.is_answered')))
    #columns.append(ColumnDT(text('prayer_request.added_by')))
    #columns.append(ColumnDT(text('prayer_request.date_added')))
    #columns.append(ColumnDT(text('prayer_request.date_answered')))
    #columns.append(ColumnDT(text('prayer_request.category_id')))

    rowTable = DataTables(params, data, columns)

    return rowTable


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

    if updatedData.date_answered != None and updatedData.date_answered != '':
        result.date_answered = updatedData.date_answered

    print(result.prayer_request_id)
    print(result.description)
    print(result.added_by)
    print(result.date_added)

    db.session.commit()

def add_prayer_request(title,description,person):
   newRequest = prayer_request()
   newRequest.title = title
   newRequest.description = description
   newRequest.is_answered = 0
   newRequest.added_by = person
   newRequest.category = 1
   newRequest.date_added = datetime.now()
   newRequest.date_answered = None

   db.session.add(newRequest)
   db.session.commit()

