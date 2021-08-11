
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

Base = declarative_base()

class category(db.Model):
    category_id = db.Column('Category_id', db.Integer, primary_key = True)
    title = db.Column("Title", db.String(50))

class category(SQLAlchemyAutoSchema):
    class Meta:
        model = category
        include_relationships = True
        load_instance = True