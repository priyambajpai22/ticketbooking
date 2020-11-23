from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()





class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password=db.Column(db.String())
    user=db.relationship('Booking')
    

    def __init__(self, email ,password):
        self.email = email
        self.password=generate_password_hash(password)
     

    def __repr__(self):
        return "{}".format(self.email)



class Seat(db.Model):
    __tablename__='seats'
    id=db.Column(db.Integer,primary_key=True)
    booked=db.Column(db.Boolean)


class Booking(db.Model):
    __tablename__='booking'
    seats=db.Column(db.Integer,db.ForeignKey('seats.id'))
    id=db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




