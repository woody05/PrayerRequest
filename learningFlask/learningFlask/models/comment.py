
from learningFlask import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

class comments(db.Model):
    comment_id = db.Column('Comment_id', db.Integer, primary_key = True)
    _comment = db.Column("Comment", db.Text)
    date_added = db.Column("Date_added", db.DateTime)

    user_id = db.Column("User_id", db.Integer, ForeignKey("users.User_id"))
    users = relationship("users")

    prayer_request_id = db.Column("Prayer_request_id", db.Integer, ForeignKey("prayer_request.Prayer_Request_id"))
    prayer_request = relationship("prayer_request", back_populates="comments")

    

def comments_for_request(id):
    result = comments.query.order_by(comment.date_added.desc())
    return result