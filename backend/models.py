from sqlalchemy import Column, Integer, String
from database import Base

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    name_start = Column(String(25), nullable=False)
    direction = Column(String(25), nullable=False)
    relation = Column(String(25), nullable=False)
    quantor = Column(String(25), nullable=False)
    name_end = Column(String(25), nullable=False)
    ring = Column(Integer)

class Rule(Base):
    __tablename__ = 'rools'
    id = Column(Integer, primary_key=True)
    directions = Column(String(50), nullable=False)
    relations = Column(String(50), nullable=False)
    quantors = Column(String(50), nullable=False)
    res_direction = Column(String(25), nullable=False)
    res_relation = Column(String(25), nullable=False)
    res_quantor = Column(String(25), nullable=False)