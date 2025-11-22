from fastapi import FastAPI

server = FastAPI()

# Simple backend endpoint that confirms request has reached
# the backend after being forwarded through the WAF
@server.get("/")
def home():
    return{"message": "Server Reached."}