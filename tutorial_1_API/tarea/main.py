#main4.py

from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/v{id}/news")
async def read_item(
    id:int, 
    desde:Optional[str]=None,
    to:Optional[str] = None,
    category: Optional[str] = None
    ):
    if id:
        return [
    {
    "id": "int",
    "title": "string",
    "url": "string",
    "date": "string",
	"media_outlet": "string",
	"category": "string"
    }]


# se puede acceder usando por ejemplo:
#GET /v1/news?from=2021-01-01&to=2021-01-31&category=sport