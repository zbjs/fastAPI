from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from prisma import Prisma

app = FastAPI()

prisma = Prisma()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate):
    return await prisma.user.create(data=user.dict())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
