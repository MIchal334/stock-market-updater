import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class OwnedStock(Base):
    __tablename__ = "owned_stocks"

    id = Column(Integer, primary_key=True)
    customer_email = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    action_amount = Column(Integer, nullable=False)  # Zmienione na Integer


engine = None


def config_database():
    global engine
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///owned_stocks.db")
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)


def create_session():
    global engine
    return sessionmaker(bind=engine)
