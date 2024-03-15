import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="127.0.0.1")
