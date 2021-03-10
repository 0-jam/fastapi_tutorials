# FastAPI Tutorials

---

1. [Environment](#environment)
1. [Installation](#installation)
  1. [macOS (Miniforge3)](#macos-miniforge3)
1. [Usage](#usage)
  1. [First Steps](#first-steps)
  1. [Path Parameters](#path-parameters)

---

## Environment

- macOS Big Sur 11.2.2 arm64
- Python 3.9.2 on Miniforge3

## Installation

### macOS (Miniforge3)

```
% conda create -n fastapi-tutorials python
% conda activate fastapi-tutorials
% conda install flake8 autopep8 fastapi uvicorn
```

## Usage

Exec `% uvicorn main:app --reload` to start the API server

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
{"item_id": 2}
```

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
