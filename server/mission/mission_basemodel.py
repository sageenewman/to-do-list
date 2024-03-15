from pydantic import BaseModel


class Mission(BaseModel):
    title: str
    priority: int
