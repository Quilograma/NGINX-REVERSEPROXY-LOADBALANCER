from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/fastapi/martim")
def read_root():
    return {"message": "Hello from Martim!"}
