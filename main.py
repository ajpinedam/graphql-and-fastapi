from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Talk(BaseModel):
    id: int
    title: str
    speaker: str
    date: str | None = None

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    category: str
    brand: str
    weight: float
    dimensions: str
    color: str
    material: str
    warranty: str
    rating: float
    reviews: int
    sku: str
    upc: str
    manufacturer: str
    model_number: str
    release_date: str
    discontinued: bool


talks : list[Talk] = [
    Talk(id=1, title="Introduction to FastAPI", speaker="Jean Phillip", date="2024-10-01"),
    Talk(id=2, title="Introduction to GraphQL", speaker="Simone", date="2024-10-11"),
    Talk(id=3, title="Python 3.13 new Features", speaker="Chloe", date="2024-11-01")
]

@app.get("/")
def read_root():
    return {"Hello": "Python Montreal!"}

@app.get("/talks")
def read_talks():
    return talks

@app.get("/talks/{talk_id}")
def read_talk(talk_id: int):
    for talk in talks:
        if talk.id == talk_id:
            return talk
    raise HTTPException(status_code=404, detail="Talk not found")