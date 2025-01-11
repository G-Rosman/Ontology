from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from pydantic import BaseModel

#engine = create_engine('sqlite:///example.db', echo=True)
#Base = declarative_base()
#Base.metadata.create_all(bind=engine)

#conn = engine.connect()
#session = sessionmaker(bind=conn)()

SQLALCHEMY_DATABASE_URL = "sqlite:///example.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    name_start = Column(String(25), nullable=False)
    direction = Column(String(25), nullable=False)
    relation = Column(String(25), nullable=False)
    quantor = Column(String(25), nullable=False)
    name_end = Column(String(25), nullable=False)
    ring = Column(Integer)

class Rool(Base):
    __tablename__ = 'rools'
    id = Column(Integer, primary_key=True)
    directions = Column(String(50), nullable=False)
    relations = Column(String(50), nullable=False)
    quantors = Column(String(50), nullable=False)
    res_direction = Column(String(25), nullable=False)
    res_relation = Column(String(25), nullable=False)
    res_quantor = Column(String(25), nullable=False)


class LinkCreate(BaseModel):
    name_start: str
    direction: str
    relation: str
    quantor: str
    name_end: str
    ring: int = None

class LinkUpdate(BaseModel):
    name_start: str | None = None
    direction: str | None = None
    relation: str | None = None
    quantor: str | None = None
    name_end: str | None = None
    ring: int | None = None




class RoolCreate(BaseModel):
    directions: str
    relations: str
    quantors: str
    res_direction: str
    res_relation: str
    res_quantor: str

class RoolUpdate(BaseModel):
    directions: str | None = None
    relations: str | None = None
    quantors: str | None = None
    res_direction: str | None = None
    res_relation: str | None = None
    res_quantor: str | None = None

    
def search_rool_db(session, directions: str, relations: str, quantors: str) -> tuple: 
    try:
        result = (
            session.query(Rool)
            .filter(
                Rool.directions == directions,
                Rool.relations == relations,
                Rool.quantors == quantors
            )
            .first()
        )
        
        if result:
            return (
                result.res_direction,
                result.res_relation,
                result.res_quantor
            )
        else:
            return None 
    except Exception as e:
        print(f"An error occurred while searching the database: {e}")
        return None
    finally:
        session.close()

def build(link1, link2, ring):
        session = Depends(get_db)
        a = search_rool_db(session, link1.direction + link2.direction, link1.relation + link2.relation, link1.quantor + link2.quantor)
        b = session.query(Link).filter_by(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end).first()
        if (a and (b == None)):
            newlink = Link(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end, ring = ring)
            session.add(newlink)
            session.commit()
            return 1
        else:
            return 0

def process_links():
    session = Depends(get_db)
    all_links = session.query(Link).all()
    flag = 0

    for current_link in all_links:
            links_to_build = session.query(Link).filter_by(name_start=current_link.name_end).all()
            # Уберу зацикливание ???
            links_to_build = [link for link in links_to_build if link.id != current_link.id]
        
            for other_link in links_to_build:
                flag += build(current_link, other_link, current_link.ring + 1)
    return flag

