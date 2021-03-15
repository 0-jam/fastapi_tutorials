from sqlalchemy.orm import Session
from . import models, schemas


# Read the database and search item by specified attributes
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Create and insert data to the database
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    # SQLAlchemy model instance
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # Add instance object to the database session
    db.add(db_user)
    # Save data to the database
    db.commit()
    # Reload instance object from the database
    db.refresh(db_user)

    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
