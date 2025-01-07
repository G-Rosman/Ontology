from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from datetime import datetime
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(bind=engine)

conn = engine.connect()
session = sessionmaker(bind=conn)()


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
    all_links = session.query(Link).all()
    flag = 0

    for current_link in all_links:
            links_to_build = session.query(Link).filter_by(name_start=current_link.name_end).all()
            # Уберу зацикливание ???
            links_to_build = [link for link in links_to_build if link.id != current_link.id]
        
            for other_link in links_to_build:
                flag += build(current_link, other_link, current_link.ring + 1)
    return flag

