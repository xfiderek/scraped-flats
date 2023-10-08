from sqlalchemy import Column, Integer, String
from database import Base


class Flat(Base):
    __tablename__ = "flats"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
