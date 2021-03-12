from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


# Create the data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


# Accept Item's attributes as JSON keys
@app.post('/items')
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})

    return item_dict
