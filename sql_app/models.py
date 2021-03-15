from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    # Declare the table name
    __tablename__ = 'users'

    # Declare attributes / columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Create the relationships
    # user.items will return a list of items
    items = relationship('Item', back_populates='owner')


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    # item.owner will return the User model object
    owner = relationship('User', back_populates='items')
