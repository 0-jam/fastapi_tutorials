# FastAPI Tutorials

---

1. [Environment](#environment)
1. [Installation](#installation)
  1. [macOS (Miniforge3)](#macos-miniforge3)
1. [Usage](#usage)
  1. [First Steps](#first-steps)
  1. [Path Parameters](#path-parameters)
    1. [Validation](#validation)
    1. [Order matters](#order-matters)
    1. [Predefined values](#predefined-values)
    1. [Path parameters containing paths](#path-parameters-containing-paths)
  1. [Query Parameters](#query-parameters)
    1. [Multiple path and query parameters](#multiple-path-and-query-parameters)
1. [Usage: GraphQL](#usage-graphql)

---

## Environment

- macOS Big Sur 11.2.2 arm64
- Python 3.9.2 on Miniforge3

## Installation

### macOS (Miniforge3)

- Initialize Conda environment

```
% conda create -n fastapi-tutorials python
% conda activate fastapi-tutorials
```

- Basic packages

```
% conda install flake8 autopep8 fastapi uvicorn
```

- Used by GraphQL

```
% conda install graphene
```

## Usage

Run `% uvicorn main:app --reload` to start the API server

`http://localhost:8000/docs` or `http://localhost:8000/redoc`: show auto-generated documents
`http://localhost:8000/openapi.json`: show OpenAPI schema

```json
{
  "openapi":"3.0.2",
  "info":{
    "title":"FastAPI","version":"0.1.0"
  },
  "paths":{
    "/":{
      "get":{
        "summary":"Root",
        "operationId":"root__get",
        "responses":{
          "200":{
            "description":"Successful Response",
            "content":{
              "application/json":{
                "schema":{}
              }
            }
          }
        }
      }
    }
  }
}
```

### First Steps

Open `http://localhost:8000`:

```json
{"message": "Hello world"}
```

### Path Parameters

Open `http://localhost:8000/items/<item_id>` (example: 2):

```json
{
  "item_id": 2,
  "description": "This is an amazing item that has a long description."
}
```

Pass an optional parameter `http://localhost:8000/items/2?q=foo`:

```json
{
  "item_id": 2,
  "q": "foo",
  "description": "This is an amazing item that has a long description."
}
```

Add `short=true` to skip the description `http://localhost:8000/items/2?short=true`:
Acceptable values (case insensitive) are:

- `true`
- `1`
- `on`
- `yes`

```json
{"item_id": 2}
```

#### Validation

When passing wrong type as an argument, you will see:

```json
{
  "detail": [
    {
      "loc": [
        "path","item_id"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

#### Order matters

`http://localhost:8000/users/me` always returns the current user information:

```json
{"user_id":"the current user"}
```

When passing other name such as `http://localhost:8000/users/jam`:

```json
{"user_id":"jam"}
```

#### Predefined values

Acceptable parameters of `http://localhost:8000/models` are declared as `Enum` object
`http://localhost:8000/models/alexnet` returns:

```json
{"model_name":"alexnet","message":"Deep Learning FTW!"}
```

`http://localhost:8000/models/alexnet` returns:

```json
{"model_name":"lenet","message":"LeCNN all the images"}
```

`http://localhost:8000/models/resnet` returns:

```json
{"model_name":"resnet","message":"Have some residuals"}
```

Other strings such as `http://localhost:8000/models/bert` returns:

```json
{
  "detail": [{
    "loc": [
      "path",
      "model_name"
    ],
    "msg": "value is not a valid enumeration member; permitted: 'alexnet', 'resnet', 'lenet'",
    "type": "type_error.enum",
    "ctx": {
      "enum_values": [
        "alexnet",
        "resnet",
        "lenet"
      ]
    }
  }]
}
```

#### Path parameters containing paths

`http://localhost:8000/files//home/jam/Documents/sample.txt` returns:

```json
{
  "file_path": "/home/jam/Documents/sample.txt"
}
```

Windows path such as `http://localhost:8000/files/C:\Users\jam\Documents\sample.txt` is also acceptable:

```json
{
  "file_path": "C:/Users/jam/Documents/sample.txt"
}
```

### Query Parameters

`http://localhost:8000/item_names/?skip=1&limiit=1` returns:

```json
[
  {"item_name": "bar"},
  {"item_name": "baz"}
]
```

#### Multiple path and query parameters

`http://localhost:8000/users/2/items/foo` returns:

```json
{
  "item_id": "foo",
  "owner_id": 2,
  "description": "This is an amazing item that has a long description."
}
```

## Usage: GraphQL

Run `% uvicorn gql:app --reload` to start the API server
Pass `http://localhost:8000` this query:

```gql
{
  hello(name: "jam")
}
```

It will return:

```json
{
  "data": {
    "hello": "Hello jam"
  }
}
```
