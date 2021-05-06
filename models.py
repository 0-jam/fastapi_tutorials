from typing import Optional, Set, List

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, Field, HttpUrl


# Submodel for Item
class Image(BaseModel):
    # String includes HTTP URL validations
    url: HttpUrl
    name: str


# Create the data model with default values
class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None,
        title="The description of the item",
        max_length=300,
    )
    price: float = Field(
        ...,
        gt=0,
        description="The price of the item (must be greater than zero)",
    )
    tax: Optional[float] = 0.1
    # Type parameters
    tags: Set[str] = []
    # Use the submodel as a type
    image: Optional[Image] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    total_price: float
    items: List[Item]


class User(BaseModel):
    name: str
    full_name: Optional[str] = None


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
    # Both item and user has the same way to pass
    item: Item = Body(..., embed=True),
    user: Optional[User] = None,
    importance: int = Body(5, gt=0),
):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})

    if item:
        results.update({'item': item, 'user': user, 'importance': importance})

    return results


@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer
