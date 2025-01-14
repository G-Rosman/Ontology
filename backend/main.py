from draw import draw
from core.config import settings
from link_class import *
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


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

@app.delete("/api/link/{id}")
async def delete_one_link(id:int):
    is_ok = delete_link(id=id)
    if is_ok is None:
        raise HTTPException(404, detail="Link not found")
    return {"message": "Link deleted successfully"}

@app.post("/api/link/update{id}")
async def update_link(link_id: int, link):
    db_link = update_one_link(id, link)
    if db_link is None:
        return HTTPException(404, detail="Link not found")
    return db_link

@app.post("/api/link/create")
async def create_link(link):
    create_one_link(link)
    return 200