from flask_marshmallow import Marshmallow
from marshmallow import Schema
from .model import Seat
from marshmallow_sqlalchemy import ModelSchema
ma = Marshmallow()


class Seatsere(ModelSchema):
	class Meta:
		model=Seat