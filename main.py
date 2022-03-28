# Create simple CRUD API with models, admin panel:
# Make an Initial Commit on the GitHub
# Create User model
# Create auth
# Create posts model
# Create comments thread

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
