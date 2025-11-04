from fastapi import FastAPI

server = FastAPI()

@server.get("/")
def home():
    return{"message": "Welcome home buddy"}