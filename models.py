from typing import Optional

from fastapi import FastAPI, Path
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


# Mixed Path, Query and body parameters
@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id: int = Path(..., title='The ID of the item to get', ge=0, le=100),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})

    if item:
        results.update({'item': item})

    return results
