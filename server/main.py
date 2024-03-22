import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

from logger.logger import initialize_logger
from mission.mission_router import mission_router

app = FastAPI()
app.include_router(mission_router)


def main():
    load_dotenv(dotenv_path=f'.\\config\\.env.{os.getenv("PYTHON_ENV")}')
    initialize_logger()
    run_server()


def run_server():
    port: int = int(os.getenv("PORT"))
    host: str = os.getenv("HOST")
    logger.info(f"server listening on port {port}")
    uvicorn.run("main:app", port=port, host=host)


if __name__ == '__main__':
    main()
