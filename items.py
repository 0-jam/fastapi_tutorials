from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


# Recieve the parameter 'q' with the default value (None) and the limit of characters (5)
@app.get('/items/')
async def read_items(
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=5,
        # Custom metadata
        # 'description' can be shown in the document
        title='Query String',
        description='Query string for the items',
        alias='item-query',
    )
):
    results = {'items': [
        {'item_id': 'Foo'},
        {'item_id': 'Bar'},
    ]}

    if q:
        results.update({'q': q})

    return results


# Recieve the parameter 'q' which accepts only the fixed value ('fixedquery') using reqular expressions
# This query is marked as deprecated (can be shown on documents)
@app.get('/items_fixed/')
async def read_items_fixed(q: Optional[str] = Query(None, min_length=3, max_length=50, regex='^fixedquery$', deprecated=True)):
    results = {'items': [
        {'item_id': 'Foo'},
        {'item_id': 'Bar'},
    ]}

    if q:
        results.update({'q': q})

    return results


# Recieve the parameter 'q' which accepts only the fixed value ('fixedquery') using reqular expressions
@app.get('/items_required/')
async def read_items_required(q: str = Query(..., min_length=3, max_length=5)):
    results = {'items': [
        {'item_id': 'Foo'},
        {'item_id': 'Bar'},
    ]}

    if q:
        results.update({'q': q})

    return results


@app.get('/items/{item_id}')
async def read_item(
    # Pass parameters as keyword arguments
    # All parameters are required
    # gt: greater than
    # lt: less than
    # ge: greater than or equal
    # le: less than or equal
    *,
    item_id: int = Path(
        ...,
        title='The ID of the item to get',
        ge=1,
        lt=100,
    ),
    q: str,
    size: float = Query(..., gt=0, le=10.5),
):
    results = {'item_id': item_id, 'size': size}

    if q:
        results.update({'q': q})

    return results
