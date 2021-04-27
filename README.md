# FastAPI Tutorials

[https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

---

1. [Environment](#environment)
1. [Installation](#installation)
    1. [Using pyenv](#using-pyenv)
1. [Usage](#usage)
    1. [First Steps](#first-steps)
    1. [Path Parameters](#path-parameters)
        1. [Validation](#validation)
        1. [Order matters](#order-matters)
        1. [Predefined values](#predefined-values)
        1. [Path parameters containing paths](#path-parameters-containing-paths)
    1. [Query Parameters](#query-parameters)
        1. [Multiple path and query parameters](#multiple-path-and-query-parameters)
    1. [Query parameters with validations](#query-parameters-with-validations)
        1. [Limit the number of characters](#limit-the-number-of-characters)
        1. [With required parameters](#with-required-parameters)
        1. [With fixed parameters](#with-fixed-parameters)
        1. [Number validations](#number-validations)
1. [Usage: GraphQL](#usage-graphql)
1. [Usage: Models](#usage-models)
    1. [Request body](#request-body)
    1. [Pass multiple parameters](#pass-multiple-parameters)
1. [Usage: SQL Databases](#usage-sql-databases)
    1. [Create user](#create-user)
    1. [Read users](#read-users)
    1. [Read single user](#read-single-user)
    1. [Create an item for the specfied user](#create-an-item-for-the-specfied-user)
    1. [Read items](#read-items)

---

## Environment

- macOS Big Sur 11.4 arm64
- Ubuntu 20.04 on WSL 2
- Python 3.9.4 on pyenv

## Installation

### Using pyenv

- Initialize Pipenv environment

```
$ pipenv --python $(which python)
```

- Basic packages

```
$ pipenv install --dev flake8 autopep8
$ pipenv install fastapi uvicorn
```

- Used by GraphQL

```
$ pipenv install graphene
```

- Used by SQL database

```
$ pipenv install sqlalchemy
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

`http://localhost:8000/item_names/?skip=1&limit=1` returns:

```json
[
  {"item_name": "bar"},
  {"item_name": "baz"}
]
```

#### Multiple path and query parameters

`http://localhost:8000/users/2/items/foo?needy=1` returns:

```json
{
  "item_id": "foo",
  "owner_id": 2,
  "needy": "1",
  "description": "This is an amazing item that has a long description."
}
```

When `needy` is missing, it returns:

```json
{
  "detail": [
    {
      "loc": ["query","needy"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Query parameters with validations

Run `% uvicorn items:app --reload` to start the API server

#### Limit the number of characters

`http://localhost:8000/items?q=Baz` returns:

parameter `q` can be replaced with `item-query`

```json
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ],
  "q": "Baz"
}
```

`http://localhost:8000/items?q=Bazbaz` fails to run and returns:

(Which accepts 3-5 characters)

```json
{
  "detail": [
    {
      "loc": [
        "query",
        "q"
      ],
      "msg": "ensure this value has at most 5 characters",
      "type": "value_error.any_str.max_length",
      "ctx": {
        "limit_value": 5
      }
    }
  ]
}
```

#### With required parameters

`http://localhost:8000/items_required` returns:

(Which tells params `q` is missing)

```json
{
  "detail": [
    {
      "loc": [
        "query",
        "q"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

`http://localhost:8000/items_required?q=Baz` works the same as [above](#limit-the-number-of-characters)

#### With fixed parameters

`http://localhost:8000/items_fixed?q=Baz` returns:

(Which only accepts `fixedquery` as the parameter `q`)

```json
{
  "detail": [
    {
      "loc": [
        "query",
        "q"
      ],
      "msg": "string does not match regex \"^fixedquery$\"",
      "type": "value_error.str.regex",
      "ctx": {
        "pattern": "^fixedquery$"
      }
    }
  ]
}
```

#### Number validations

`http://localhost:8000/items/10?q=foo&size=1` returns:

```json
{
  "item_id": 10,
  "size": 1.0,
  "q": "foo"
}
```

`http://localhost:8000/items/111?size=11` fails to run and returns:

```json
{
  "detail": [
    {
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "ensure this value is less than 100",
      "type": "value_error.number.not_lt",
      "ctx": {
        "limit_value": 100
      }
    },
    {
      "loc": [
        "query",
        "q"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": [
        "query",
        "size"
      ],
      "msg": "ensure this value is less than or equal to 10.5",
      "type": "value_error.number.not_le",
      "ctx": {
        "limit_value": 10.5
      }
    }
  ]
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

## Usage: Models

Run `% uvicorn models:app --reload` to start the API server

### Request body

Post `http://localhost:8000/items` this JSON:

```json
{
  "name": "sample",
  "description": "my first item",
  "price": 100,
  "tax": 8
}
```

It will return created model with the calculated price with tax:

```json
{
  "name": "sample",
  "description": "my first item",
  "price": 100.0,
  "tax": 8.0,
  "price_with_tax": 108.0
}
```

Attributes `description` and `tax` are nullable:

```json
{
  "name": "sample",
  "price": 100
}
```

...and will not calculate price with tax:

```json
{
  "name": "sample",
  "description": null,
  "price": 100.0,
  "tax": null
}
```

### Pass multiple parameters

`http://localhost:8000/items/3?q=foo` with this JSON:

```json
{
    "item": {
        "name": "sample",
        "price": 100,
        "description": "A sample item"
    },
    "user": {
        "name": "0-jam",
        "full_name": "aozamemaou"
    },
    "importance": 3
}
```

It returns:

```json
{
  // Passed as parameters
  "item_id": 3,
  "q": "foo",
  // Passed as JSON
  "item": {
    "name": "sample",
    "description": "A sample item",
    "price": 100.0,
    "tax": 0.1
  },
  "user": {
    "name": "0-jam",
    "full_name": "aozamemaou"
  },
  "importance": 3
}
```

## Usage: SQL Databases

Run `% uvicorn sql_app.main:app --reload` to start the API server

### Create user

Post `http://localhost:8000/users`:

```json
{
  "email": "sample@example.com",
  "password": "password"
}
```

It will return created `User`:

```json
{
  "email": "sample@example.com",
  "id": 1,
  "is_active": true,
  "items": []
}
```

### Read users

Get `http://localhost:8000/users` then it will returns a list of created users:

```json
[
  {
    "email": "sample@example.com",
    "id": 1,
    "is_active": true,
    "items": []
  },
  {
    "email": "sample2@example.com",
    "id": 2,
    "is_active": true,
    "items": []
  }
]
```

### Read single user

Get `http://localhost:8000/users/1` then it will returns the user specified by its ID:

```json
{
  "email": "sample@example.com",
  "id": 1,
  "is_active": true,
  "items": []
}
```

### Create an item for the specfied user

Post `http://localhost:8000/users/1/items`:

```json
{
  "title": "sample item",
  "description": "my first item"
}
```

It will returns the created `Item` associated with the specified user:

```json
{
  "title": "sample item",
  "description": "my first item",
  "id": 1,
  "owner_id": 1
}
```

### Read items

Get `http://localhost:8000/items` then it will returns a list of created items:

```json
[
  {
    "title": "sample item",
    "description": "my first item",
    "id": 1,
    "owner_id": 1
  },
  {
    "title": "sample item 2",
    "description": "second user's item",
    "id": 2,
    "owner_id": 2
  }
]
```
