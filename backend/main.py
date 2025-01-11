from draw import draw
from core.config import settings
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException
import os
from db import Link, Rool, get_db, LinkCreate, LinkUpdate, RoolCreate, RoolUpdate
from crud import *


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get("/api/graph")
async def graph():
    draw()
    image_path = "output.png"
    if not os.path.exists(image_path):
        return {"error": "Image not found"}, 404
    return FileResponse(image_path, media_type="image/png", filename=image_path)


router = APIRouter()
"""
@router.post("/links/", response_model=Link)
def create_link(link: LinkCreate, db: Session = Depends(get_db)):
    return create_link(db, link)

@router.get("/links/{link_id}", response_model=Link)
def read_link(link_id: int, db: Session = Depends(get_db)):
    link = get_link(db, link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

@router.put("/links/{link_id}", response_model=Link)
def update_link(link_id: int, link: LinkUpdate, db: Session = Depends(get_db)):
    current_link = get_link(db, link_id)
    if current_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    update_link(db, link)
    return current_link

@router.delete("/links/{link_id}")
def delete_link(link_id: int, db: Session = Depends(get_db)):
    link = get_link(db, link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    delete_link(db, link_id)
    return {"message": "Link deleted successfully"}
"""
# Аналогичные эндпоинты для таблицы Rool:

# @router.post("/rools/", response_model=Rool)
# def create_rool(rool: RoolCreate, db: Session = Depends(get_db)):
#     return create_rool(db, rool)

# @router.get("/rools/{rool_id}", response_model=Rool)
# def read_rool(rool_id: int, db: Session = Depends(get_db)):
#     rool = get_rool(db, rool_id)
#     if rool is None:
#         raise HTTPException(status_code=404, detail="Rool not found")
#     return rool

# @router.put("/rools/{rool_id}", response_model=Rool)
# def update_rool(rool_id: int, rool: RoolUpdate, db: Session = Depends(get_db)):
#     current_rool = get_rool(db, rool_id)
#     if current_rool is None:
#         raise HTTPException(status_code=404, detail="Rool not found")
#     update_rool(db, rool)
#     return current_rool

# @router.delete("/rools/{rool_id}")
# def delete_rool(rool_id: int, db: Session = Depends(get_db)):
#     rool = get_rool(db, rool_id)
#     if rool is None:
#         raise HTTPException(status_code=404, detail="Rool not found")
#     delete_rool(db, rool_id)
#     return {"message": "Rool deleted successfully"}

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