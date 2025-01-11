from sqlalchemy.orm import Session
from db import Link, Rool, get_db

def create_link(db: Session, link: Link):
    db_link = Link(**link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def get_link(db: Session, link_id: int):
    return db.query(Link).filter(Link.id == link_id).first()

def update_link(db: Session, link: Link):
    db.query(Link).filter(Link.id == link.id).update(link.__dict__)
    db.commit()

def delete_link(db: Session, link_id: int):
    db.query(Link).filter(Link.id == link_id).delete()
    db.commit()

def create_rool(db: Session, rool: Rool):
    db_rool = Rool(**rool.dict())
    db.add(db_rool)
    db.commit()
    db.refresh(db_rool)
    return db_rool

def get_rool(db: Session, rool_id: int):
    return db.query(Rool).filter(Rool.id == rool_id).first()

def update_rool(db: Session, rool: Rool):
    db.query(Rool).filter(Rool.id == rool.id).update(rool.__dict__)
    db.commit()

def delete_rool(db: Session, rool_id: int):
    db.query(Rool).filter(Rool.id == rool_id).delete()
    db.commit()
