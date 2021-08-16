
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class category(db.Model):
    category_id = db.Column('Category_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.String(50))


def all_categories():
    result = category.query.order_by(category.title.asc())
    return result