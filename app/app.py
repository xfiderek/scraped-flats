from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import subprocess
import models
from database import engine, get_db
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def initialize():
    # init db schema
    models.Base.metadata.create_all(bind=engine)
    # run crawler
    subprocess.run(
        ["scrapy crawl flat"], shell=True, check=True, capture_output=True
    )


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, db: Session = Depends(get_db)):
    flats = db.query(models.Flat).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "flats": flats}
    )
