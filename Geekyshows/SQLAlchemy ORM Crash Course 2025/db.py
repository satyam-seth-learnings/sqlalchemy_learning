from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///sqlite.db"

# if echo true sqlalchemy print generate sql queries in terminal
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
