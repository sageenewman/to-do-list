import uvicorn
from fastapi import FastAPI
from logger.logger import initialize_logger

app = FastAPI()


def main():
    initialize_logger()
    run_server()


def run_server():
    uvicorn.run("main:app", port=8080, host="127.0.0.1")


if __name__ == '__main__':
    main()
