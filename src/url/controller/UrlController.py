from fastapi import FastAPI, status, Request
from src.url.schemas.UrlSchemas import *
from src.url.repository.UrlRepository import UrlRepository

app = FastAPI()

database = UrlRepository()

@app.post("/", status_code=status.HTTP_201_CREATED, response_model=Url, description="Create a new short URL")
def create_url(url_payload: CreateUrl, request: Request):
    return {}

@app.get("/", status_code=status.HTTP_200_OK, response_model=list[Url], description="Get all URLs")
def getAllURLs():
    return list(database.values())

@app.get("/{url_id}", status_code=status.HTTP_200_OK, response_model=Url, description="Get URL")
def getURLData(url_id: str):
    return database.get(url_id)

@app.put()
def updateUrl():
    return {}

@app.delete()
def deleteUrl():
    return {}
