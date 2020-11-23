from src.model import Seat,db


def prepopulate():
	if Seat.query.all()!=[]:
		data=db.session()
		objects=[]
		for x in range(0,8):
			objects.append(Seat(booked=False))
		data.bulk_save_objects(objects)
		data.commit()
