
from flask.views import View
from flask import render_template ,redirect
from .model import User,db,Seat,Booking
from flask import request
from .authentication import is_authenticated,user_required
from .forms import UserForm
from flask import flash,jsonify
from app.data_prepopulate import prepopulate
from flask import Flask, redirect, url_for, session
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from .serailizer import Seatsere


class Index(MethodView):

    def get(self):
        
        return render_template('login.html')


    def post(self):
    	log=is_authenticated(**dict(request.form))
    	if log==True:

    		return redirect(url_for('booking'))
    	else:
    		return render_template('login.html', data={'error':'invalid email or password'})



class Signup(MethodView):

	def __init__(self):
		self.template='signup.html'
		self.form=UserForm()
	def get(self):
		
		return render_template(self.template,form=self.form)

	def post(self):
		if self.form.validate_on_submit():
			data=(dict(request.form))
			data.pop('csrf_token')
			data=User(**data)

			db.session.add(data)
			db.session.commit()
			flash('Thanks for registering')
			return redirect('login')

		
		return render_template(self.template, form=self.form)





class BookingView(MethodView):
	decorators = [user_required]

	def get (self):
		data=Seat.query.all()
		return render_template('booking.html',data=data)

	def post(self):
		seat=Seat.query.filter_by(id=request.form['id']).first()
		bookingdata=Booking.query.filter_by(seats=seat.id).first()
		if bookingdata!=None:
			if bookingdata.user_id!=request.user.id:
				return jsonify({'error':'this seat is taken by someone'})
			else:
				seat.booked=False
				db.session.delete(bookingdata)
				db.session.commit()
				return jsonify({'unbook':'seat has been unbook'})
		data=Booking(user_id=request.user.id,seats=request.form['id'])
		db.session.add(data)
		db.session.commit()
		
		seat.booked=True
		db.session.commit()
		serailizer_obj=Seatsere()
		return serailizer_obj.dump(seat)



class Logout(MethodView):
	def get(self):
		session.clear()
		return  redirect('login')





