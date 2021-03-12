from enum import Enum
from typing import Optional

from fastapi import FastAPI


# Set acceptable values as the subclass of str and Enum
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


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
async def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, q: q}

    return {'item_id': item_id}


fake_item_db = [
    {'item_name': 'foo'},
    {'item_name': 'bar'},
    {'item_name': 'baz'},
]


# Declare query parameters with default values
# Going to /items/ is the same as going to /items/?skip=0&limit=10
@app.get('/item_names/')
async def read_item_names(skip: int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]


# A fixed path example
# A fixed path must be declared before other variable paths
@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


# Accept values that is declared above
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


# Pass file_path as a parameter
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
