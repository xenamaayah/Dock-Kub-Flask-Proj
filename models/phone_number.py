from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from database import db


class PhoneNumber(db.Model):
    __tablename__ = "PhoneNumber"

    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)
    number = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    user = db.relationship('User', back_populates='phone_numbers', overlaps="user")

    def __repr__(self):
        return f"Phone Number('{self.number}')"
