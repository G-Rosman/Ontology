from draw import draw
from core.config import settings
from link_class import *
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
import os

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)



@app.get("/")
def hello_api():
    return {"msg":"Привет FastAPI🚀"}


@app.get("/api/graph")
async def graph():
    draw()
    image_path = "output.png"
    if not os.path.exists(image_path):
        return {"error": "Image not found"}, 404
    return FileResponse(image_path, media_type="image/png", filename="output.png")



@app.get("/api/links")
async def show_links():
    links =  show_all_links()
    return {"links": links}, 200

@app.get("/api/links/{id}")
async def show_one_link(id:int):
    link = show_one_link(id)
    return {"link": link}, 200

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