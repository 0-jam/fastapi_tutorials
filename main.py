from fastapi import FastAPI
from enum import Enum


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
async def read_item(item_id: int):
    return {'item_id': item_id}


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
