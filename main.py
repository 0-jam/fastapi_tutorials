from fastapi import FastAPI

# Generate a FastAPI instance
app = FastAPI()


# Define a path to access this instance
# 'get' means HTTP GET
# and execute the function at the next line
@app.get('/')
async def root():
    return {'message': 'Hello world'}


# Pass 'item_id' as arguments of the function
@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id': item_id}
