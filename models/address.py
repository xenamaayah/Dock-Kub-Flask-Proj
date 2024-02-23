from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from database import db


class Address(db.Model):
    __tablename__ = "Address"

    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    street = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    postal_code = Column(String(255), nullable=False)

    user_ref = db.relationship('User', back_populates='address', overlaps="user")

    def __repr__(self):
        return f"Address('{self.street}, {self.city}, {self.state}, {self.postal_code}')"

