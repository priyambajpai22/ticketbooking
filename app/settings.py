from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.views import Index,Signup,BookingView,Logout
app=Flask(__name__,template_folder='../template')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/ticket"
app.secret_key = 'priyambajpai'
db = SQLAlchemy(app)
migrate = Migrate(app, db)









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
    booked=db.Column(db.Boolean,default=False)


class Booking(db.Model):
    __tablename__='booking'
    seats=db.Column(db.Integer,db.ForeignKey('seats.id'))
    id=db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




app.add_url_rule('/login', view_func=Index.as_view('login'))
app.add_url_rule('/signup', view_func=Signup.as_view('signup'))
app.add_url_rule('/booking',view_func=BookingView.as_view('booking'))
app.add_url_rule('/logout',view_func=Logout.as_view('logout'))



