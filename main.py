from typing import Optional
import strawberry

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from strawberry.fastapi import GraphQLRouter

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

talks: list[Talk] = [
    Talk(id=1, title="Introduction to FastAPI", speaker="Jean Phillip", date="2024-10-01"),
    Talk(id=2, title="Introduction to GraphQL", speaker="Simone", date="2024-10-11"),
    Talk(id=3, title="Python 3.13 new Features", speaker="Chloe", date="2024-11-01"),
    Talk(id=4, title="Machine Learning Basics", speaker="Alice", date="2024-11-15"),
    Talk(id=5, title="Deep Learning with TensorFlow", speaker="Bob", date="2024-11-20"),
    Talk(id=6, title="Data Science with Python", speaker="Carol", date="2024-11-25"),
    Talk(id=7, title="Building APIs with Django", speaker="Dave", date="2024-12-01"),
    Talk(id=8, title="Introduction to Docker", speaker="Eve", date="2024-12-05")
]

products: list[Product] = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, stock=50, category="Electronics", brand="BrandA", weight=2.5, dimensions="30x20x2 cm", color="Silver", material="Aluminum", warranty="1 year", rating=4.5, reviews=150, sku="LAP123", upc="123456789012", manufacturer="BrandA Inc.", model_number="LAP12345", release_date="2023-01-01", discontinued=False),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=799.99, stock=100, category="Electronics", brand="BrandB", weight=0.2, dimensions="15x7x0.8 cm", color="Black", material="Glass", warranty="2 years", rating=4.7, reviews=200, sku="SMP456", upc="123456789013", manufacturer="BrandB Inc.", model_number="SMP45678", release_date="2023-05-01", discontinued=False),
    Product(id=3, name="Tablet", description="A powerful tablet", price=499.99, stock=75, category="Electronics", brand="BrandC", weight=0.5, dimensions="25x17x0.7 cm", color="Gold", material="Metal", warranty="1 year", rating=4.3, reviews=120, sku="TAB789", upc="123456789014", manufacturer="BrandC Inc.", model_number="TAB78901", release_date="2023-03-01", discontinued=False),
    Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=199.99, stock=200, category="Wearables", brand="BrandD", weight=0.1, dimensions="4x4x1 cm", color="Black", material="Plastic", warranty="1 year", rating=4.6, reviews=180, sku="SWT012", upc="123456789015", manufacturer="BrandD Inc.", model_number="SWT01234", release_date="2023-02-01", discontinued=False),
    Product(id=5, name="Headphones", description="Noise-cancelling headphones", price=299.99, stock=150, category="Audio", brand="BrandE", weight=0.3, dimensions="20x18x5 cm", color="White", material="Plastic", warranty="2 years", rating=4.8, reviews=220, sku="HDP345", upc="123456789016", manufacturer="BrandE Inc.", model_number="HDP34567", release_date="2023-04-01", discontinued=False),
    Product(id=6, name="Camera", description="A high-resolution camera", price=899.99, stock=30, category="Photography", brand="BrandF", weight=1.2, dimensions="15x10x8 cm", color="Black", material="Metal", warranty="1 year", rating=4.7, reviews=90, sku="CAM678", upc="123456789017", manufacturer="BrandF Inc.", model_number="CAM67890", release_date="2023-06-01", discontinued=False),
    Product(id=7, name="Monitor", description="A 4K UHD monitor", price=399.99, stock=40, category="Computers", brand="BrandG", weight=5.0, dimensions="60x40x5 cm", color="Black", material="Plastic", warranty="3 years", rating=4.4, reviews=110, sku="MON901", upc="123456789018", manufacturer="BrandG Inc.", model_number="MON90123", release_date="2023-07-01", discontinued=False)
]

@strawberry.type
class ProductType:
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

@strawberry.type
class TalkType:
    id: int
    title: str
    speaker: str
    date: str

app = FastAPI()

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


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello Python Montreal!"

    @strawberry.field
    def products(self) -> list[ProductType]:
        return products

    @strawberry.field
    def product_by_id(self, id: int) -> Optional[ProductType]:
        for product in products:
            if product.id == id:
                return product
        return None

    @strawberry.field
    def talks(self) -> list[TalkType]:
        return talks
    
    @strawberry.field
    def talks_by_id(self, id: int) -> Optional[TalkType]:
        for talk in talks:
            if talk.id == id:
                return talk
        return None
    

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
