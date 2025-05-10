from sqlalchemy import select

from models import User
from db import SessionLocal


# Insert Data
def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()


# Fetch Single Data
def get_single_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        return user


# Fetch All Data
def get_all_user():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users


# Update Data
def update_user_email(user_id: int, new_email: str):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
    return user


# Delete Data
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
