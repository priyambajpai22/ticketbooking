from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from flask import Flask, session
from flask import request,redirect,url_for



def is_authenticated(email,password):
    	#import pdb;pdb.set_trace()
    	user=User.query.filter_by(email=email).first()
    	if user!=None:
    		data=check_password_hash(user.password,password)
    		if data==True:
    			session['user']=user.id
    			#import pdb;pdb.set_trace()
    			return True

    	return False






def user_required(f):
	def decorator(*args, **kwargs):
		#import pdb;pdb.set_trace()
		if 'user' in session:
			if session['user']!=None:
				print(session['user'])
				request.user=User.query.filter_by(id=session['user']).first()
				
				
		else:
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return decorator