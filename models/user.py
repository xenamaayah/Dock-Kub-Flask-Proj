from sqlalchemy import (
    Column,
    Integer,
    String,
)
from database import db
from models.address import Address
from models.phone_number import PhoneNumber


class User(db.Model):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(255), nullable=False)
    address = db.relationship(Address, back_populates='user_ref', lazy='joined', cascade='all, delete')
    phone_numbers = db.relationship(PhoneNumber, back_populates='user', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"User('{self.address}')!"
