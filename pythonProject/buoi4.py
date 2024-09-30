from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Định nghĩa request model
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

# Định nghĩa response model
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

# API nhận dữ liệu sản phẩm và trả về JSON theo response model
@app.post("/products", response_model=ProductResponse)
async def create_product(product: Product):
    return product
