from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

# Example of a mock user database
fake_user_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@x.com",
        "full_name": "John Doe",
        "is_active": True,
        "is_superuser": True,
        "is_verified": True,
    }
}

class User(BaseModel):
    username: str
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
def read_user_me():
    return fake_user_db["johndoe"]

@app.post('/create-user')
def create_user(user: User):
    fake_user_db[user.username] = user.dict()
    return {"user": user}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
