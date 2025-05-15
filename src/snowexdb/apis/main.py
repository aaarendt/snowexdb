from fastapi import FastAPI
from snowexdb.repositories.base_repository import BaseRepository
from snowexdb.models.doi import DOI
from snowexdb.models.site import Site
from snowexdb.utils.projection import create_box

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the SnowExDB API!"}

@app.get("/dois/")
async def getDOIS():
    t = BaseRepository.select_all(DOI)
    return {"data": t}

@app.get("/spatial/")
async def getSpatial(xmin: float, ymin: float, xmax: float, ymax: float):
    bbox = create_box(xmin, ymin, xmax, ymax,4326)
    t = BaseRepository.spatial_select(Site, bbox)
    return {"data": t}