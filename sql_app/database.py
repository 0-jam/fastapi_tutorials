from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to the SQLite database file
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# URL to the PostgreSQL database
# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'

# Initialize the SQLAlchemy engine
# 'check_same_thread' is needed only for SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class used for ORM models
Base = declarative_base()
