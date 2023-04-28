
# fastapi-rest

RESTful APIs with Python using FastAPI framework


## Run Locally

Clone the project

```bash
  git clone https://github.com/muntamehtaz/fastapi-rest.git
```

Go to the project directory

```bash
  cd fastapi-rest
```

Install dependencies in pyhton virtual environment

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```


## API Reference

#### Get all users

```http
  GET /api/v1/users
```

#### Create user

```http
  POST /api/v1/users
```

#### Update user

```http
  PUT /api/v1/users${user_id}
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `user_id` | `string` | **Required**. Id of user to update |

#### Delete user

```http
  DELETE /api/v1/users${user_id}
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `user_id` | `string` | **Required**. Id of user to delete |



## Tech Stack

**Server:** Python, FastAPI, Uvicorn


