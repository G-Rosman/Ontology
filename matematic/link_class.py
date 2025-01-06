from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

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

engine = create_engine('sqlite:///example.db', echo=True)

Base.metadata.create_all(bind=engine)

def add_data(session):
    pass
    #link1 = Link(name_start="Instruments", direction="L", relation="5", quantor="aa", name_end="binary_vulns", ring = 0)
    #link2 = Link(name_start="Instruments", direction="R", relation="13", quantor="aa", name_end="Static", ring = 0)
    #link3 = Link(name_start="Instruments", direction="R", relation="13", quantor="aa", name_end="Symbolic", ring = 0)
    #link4 = Link(name_start="Instruments", direction="R", relation="13", quantor="aa", name_end="Dynamic", ring = 0)
    #link5 = Link(name_start="Static", direction="R", relation="13", quantor="aa", name_end="Ida", ring = 0)
    #link6 = Link(name_start="Static", direction="R", relation="13", quantor="aa", name_end="Ghidra", ring = 0)
    #link7 = Link(name_start="Static", direction="R", relation="13", quantor="aa", name_end="Radare", ring = 0)
    #link8 = Link(name_start="Dynamic", direction="R", relation="13", quantor="aa", name_end="edb", ring = 0)

    #session.add_all([link1, link2, link3, link4, link5, link6, link7, link8])
    
    #rool = Rool(directions="RR", relations="1313", quantors="aaaa", res_direction="R", res_relation="13", res_quantor="aa")
    #from full import parse_json_to_list, json_data
    #l = parse_json_to_list(json_data)
    #for i in l:
    #    rool = Rool(directions=i[0], relations=i[1], quantors=i[2], res_direction=i[3], res_relation=i[4], res_quantor=i[5])
    #    session.add(rool)


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
            return None  # No matching rule found
    except Exception as e:
        print(f"An error occurred while searching the database: {e}")
        return None
    finally:
        session.close()

def build(session, link1, link2, ring):
        a = search_rool_db(session, link1.direction + link2.direction, link1.relation + link2.relation, link1.quantor + link2.quantor)
        b = session.query(Link).filter_by(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end).first()
        if (a and (b == None)):
            newlink = Link(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end, ring = ring)
            session.add(newlink)
            session.commit()
            return 1
        else:
            return 0

def process_links(session):
    all_links = session.query(Link).all()
    flag = 0

    for current_link in all_links:
            links_to_build = session.query(Link).filter_by(name_start=current_link.name_end).all()
            # Уберу зацикливание ???
            links_to_build = [link for link in links_to_build if link.id != current_link.id]
        
            for other_link in links_to_build:
                flag += build(session, current_link, other_link, current_link.ring + 1)
    return flag



def count():
    with engine.connect() as conn:
        session = sessionmaker(bind=conn)()
    #add_data(session)
        session.commit()

        while (process_links(session)):
            pass

