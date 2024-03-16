import uvicorn
from fastapi import FastAPI
from loguru import logger

from app_config import APP, PORT, HOST
from logger.logger import initialize_logger
from mission.mission_router import mission_router

app = FastAPI()
app.include_router(mission_router)


def main():
    initialize_logger()
    run_server()


def run_server():
    logger.info(f"server listening on port {PORT}")
    uvicorn.run(APP, port=PORT, host=HOST)


if __name__ == '__main__':
    main()
