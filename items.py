from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


# Recieve the parameter 'q' with the default value (None) and the limit of characters (5)
@app.get('/items/')
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=5)):
    results = {'items': [
        {'item_id': 'Foo'},
        {'item_id': 'Bar'},
    ]}

    if q:
        results.update({'q': q})

    return results
