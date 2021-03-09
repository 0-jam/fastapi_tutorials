# FastAPI Tutorials

## Installation

### macOS (Miniforge3)

```
% conda create -n fastapi-tutorials python
% conda activate fastapi-tutorials
% conda install flake8 autopep8 fastapi uvicorn
```

## Usage

Exec `% uvicorn main:app --reload` and open `http://localhost:8000`

```json
{
    "message": "Hello world"
}
```

Open `http://localhost:8000/docs` or `http://localhost:8000/redoc` to show auto-generated documents
Open `http://localhost:8000/openapi.json` to OpenAPI schema

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
