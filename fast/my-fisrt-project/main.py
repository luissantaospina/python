from fastapi import FastAPI, Query
from typing import Optional
from User import User

app = FastAPI(
    title='My fist project',
    description='My fist project',
    version='1.0.0'
)


@app.get("/")
def home():
    return {"message": "Hello word!"}


# with params and body
@app.get("/user/{user_id}")
def get_user(user_id: int, query: Optional[str] = 8):
    return {"user_id": user_id, "query": query}


# with body and validations
@app.post("/users")
def create_user(user: User):
    return {"username": user.username, "phone": user.phone}


# with body, validations and validation query
# Query have many arguments for use, min, max, len
@app.post("/users_query")
def create_user_param(user: User, is_activate: bool = Query(False)):
    return {"username": user.username, "phone": user.phone, "is_activate": is_activate}
