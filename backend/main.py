from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import FileResponse
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import os
import subprocess
from sqlalchemy import select
from sqlalchemy.sql import Select

Base.metadata.create_all(engine)

app = FastAPI()
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.post("/api/link", response_model=schemas.Link, status_code=status.HTTP_201_CREATED)
def create_link(link: schemas.LinkCreate, session: Session = Depends(get_session)):
    linkdb = models.Link(name_start = link.name_start, direction = link.direction, relation = link.relation,
                        quantor = link.quantor, name_end = link.name_end, ring = link.ring)
    session.add(linkdb)
    session.commit()
    session.refresh(linkdb)
    return linkdb

@app.get("/api/link/{id}", response_model=schemas.Link)
def read_link(id: int, session: Session = Depends(get_session)):
    link = session.query(models.Link).get(id)
    if not link:
        raise HTTPException(status_code=404, detail=f"link item with id {id} not found")
    return link

@app.put("/api/update/link/{id}", response_model=schemas.Link)
def update_link(id: int, link_data: schemas.LinkCreate, session: Session = Depends(get_session)):
    linkdb = session.query(models.Link).get(id)
    if linkdb:
        for key, value in link_data.dict().items():
            setattr(linkdb, key, value)
        session.commit()
    if not linkdb:
        raise HTTPException(status_code=404, detail=f"link item with id {id} not found")
    return linkdb

@app.delete("/api/delete/link/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(id: int, session: Session = Depends(get_session)):
    link = session.query(models.Link).get(id)
    if link:
        session.delete(link)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"link item with id {id} not found")
    return None

@app.get("/api/links", response_model = List[schemas.Link])
def read_link_list(session: Session = Depends(get_session)):
    link_list = session.query(models.Link).all()
    return link_list

@app.post("/api/rule", response_model=schemas.Rule, status_code=status.HTTP_201_CREATED)
def create_rule(rule: schemas.RuleCreate, session: Session = Depends(get_session)):
    ruledb = models.Rule(directions = rule.directions, relations = rule.relations, quantors = rule.quantors,
                        res_direction = rule.res_direction, res_quantor = rule.res_quantor, res_relation = rule.res_relation)
    session.add(ruledb)
    session.commit()
    session.refresh(ruledb)
    return ruledb

@app.get("/api/rule/{id}", response_model=schemas.Rule)
def read_rule(id: int, session: Session = Depends(get_session)):
    rule = session.query(models.Rule).get(id)
    if not rule:
        raise HTTPException(status_code=404, detail=f"link item with id {id} not found")
    return rule

@app.put("/api/update/rule/{id}", response_model=schemas.Rule)
def update_rule(id: int, rule_data: schemas.RuleCreate, session: Session = Depends(get_session)):
    ruledb = session.query(models.Rule).get(id)
    if ruledb:
        for key, value in rule_data.dict().items():
            setattr(ruledb, key, value)
        session.commit()
    if not ruledb:
        raise HTTPException(status_code=404, detail=f"rule item with id {id} not found")
    return ruledb

@app.delete("/api/delete/rule/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rule(id: int, session: Session = Depends(get_session)):
    rule = session.query(models.Rule).get(id)
    if rule:
        session.delete(rule)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"rule item with id {id} not found")
    return None

@app.get("/api/rules", response_model = List[schemas.Rule])
def read_rules_list(session: Session = Depends(get_session)):
    rule_list = session.query(models.Rule).all()
    return rule_list



def search_rool_db(directions: str, relations: str, quantors: str, session: Session) -> tuple:
    try: 
        result = (
            session.query(models.Rule)
            .filter(
                models.Rule.directions == directions,
                models.Rule.relations == relations,
                models.Rule.quantors == quantors
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


def build(link1, link2, ring, session: Session):
        a = search_rool_db(link1.direction + link2.direction, link1.relation + link2.relation, link1.quantor + link2.quantor, session)
        b = session.query(models.Link).filter_by(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end).first()
        if (a and (b == None)):
            newlink = models.Link(name_start=link1.name_start, direction=a[0], relation=a[1], quantor=a[2], name_end=link2.name_end, ring = ring)
            session.add(newlink)
            session.commit()
            return 1
        else:
            return 0
        

def process_links(session: Session):
    all_links = session.query(models.Link).all()
    flag = 0

    for current_link in all_links:
            links_to_build = session.query(models.Link).filter_by(name_start=current_link.name_end).all()
            # Уберу зацикливание ???
            links_to_build = [link for link in links_to_build if link.id != current_link.id]
        
            for other_link in links_to_build:
                flag += build(current_link, other_link, current_link.ring + 1, session=session)
    return flag

def generate_graph(session: Session) -> str:
    """
    Генерирует граф в формате DOT на основе данных из базы данных.
    
    :param db_path: Путь к SQLite базы данных
    :return: Текст графического представления в формате DOT
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM links ORDER BY name_start, name_end")
    rows = cursor.fetchall()
    """
    # stmt: Select = select(models.Link).order_by(models.Link.name_start, models.Link.name_end)
    
    # # Получаем результат запроса
    # result = session.execute(stmt)
    # rows = result.all()
    rows = session.query(models.Link).all()
    # Генерируем граф
    graph = "digraph G {\n"
    graph += "node[color = black, fontsize = 12];\n"
    graph += "edge[color = black, fontsize = 12];\n"

    for row in rows:
        print(row)
        print(row.name_start, row.direction, row.quantor, row.relation, row.name_end, row.ring)
        start, direction, rool, quantor, end, ring = row.name_start, row.direction,  row.relation, row.quantor, row.name_end, row.ring
        graph += f'"{start}" -> "{end}" [dir=both,color = '
        if (rool == "5"):  
            graph += "blue,"
        elif (rool == "13"):
            graph += "black,"
        elif (rool == "7"):
            graph += "red,"

        if ring:
            graph += "style = dotted, "

        if quantor == "aa":
            graph += "arrowhead=normal, arrowtail=box"
        elif quantor == "ae":
            graph += "arrowhead=normal, arrowtail=obox"
        elif quantor == "ea":
            graph += "arrowhead=onormal, arrowtail=box"
        elif quantor == "ee":
            graph += "arrowhead=onormal, arrowtail=obox"

        graph += "];\n"
    graph += "}\n"

    return graph


def draw(session: Session):
    while (process_links(session=session)):
        pass

    dot_file_path = "graph.dot"
    picture = "output.png"

    graph_text = generate_graph(session)

    with open(dot_file_path, "w") as f:
        f.write(graph_text)

    cmd = ['dot', '-Tpng', dot_file_path, '-o', picture]
    subprocess.run(cmd, capture_output=True, text=True, check=True)

@app.get("/api/graph")
async def graph():
    draw(session = next(get_session()))
    image_path = "output.png"
    if not os.path.exists(image_path):
         return {"error": "Image not found"}, 404
    return FileResponse(image_path, media_type="image/png", filename="output.png")
