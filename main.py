from typing import List
import sqlalchemy.orm as _orm
from fastapi import FastAPI, Depends, HTTPException

import services as _services, schemas as _schemas

# Create simple CRUD API with models, admin panel:
# Create posts model
# Create comments thread

app = FastAPI()
_services.create_database()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/users/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = Depends(_services.get_db)
):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return _services.create_user(db=db, user=user)


@app.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int, db: _orm.Session = Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user

