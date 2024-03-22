from fastapi import APIRouter

from app_config import TO_DO_LIST_DB, MISSIONS_COLLECTION
from dbs.db_client.abstract_client import DBClient
from dbs.mongo_db.mongo_connection import MongoClient
from dbs.mongo_db.mongo_query_executor import MongoQueryExecutor
from mission.mission_basemodel import Mission

mission_router = APIRouter()


@mission_router.post('/create-mission')
def create_mission(mission: Mission):
    mongo_client: DBClient = MongoClient(LOCAL_MONGO)
    query_executor: MongoQueryExecutor = MongoQueryExecutor(mongo_client.client)
    query_executor.set_db(TO_DO_LIST_DB)
    query_executor.set_collection(MISSIONS_COLLECTION)
    query_executor.create(query=mission.dict())
    return mission
