from typing import List, Optional

from pydantic import BaseModel


# Create Pydantic models (schemas)
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


# Add additional attributes to ItemBase
class ItemCreate(ItemBase):
    pass


# Schema for reading or returning data from the API
class Item(ItemBase):
    id: int
    owner_id: int

    # Turn on ORM mode
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    # User will have a password when creating it
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
