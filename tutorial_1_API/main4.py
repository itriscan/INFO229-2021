#main4.py

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# se puede acceder usando por ejemplo:
#  http://127.0.0.1:8000/items/2?q=askdjakld
