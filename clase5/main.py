from fastapi import FastAPI
from pydantic import BaseModel


class Hello(BaseModel):
    name: str
    message: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.post("/santy", tags=["sanity"])
def say_hello(Hellos: Hello):
    return Hellos

