from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from db import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"


def create_table():
    Base.metadata.create_all(engine)
