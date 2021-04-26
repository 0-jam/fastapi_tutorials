from typing import Optional

from fastapi import FastAPI, Query

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
@app.get('/items_fixed/')
async def read_items_fixed(q: Optional[str] = Query(None, min_length=3, max_length=50, regex='^fixedquery$')):
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
