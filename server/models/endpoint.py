from pydantic import BaseModel


class Endpoint(BaseModel):
    endpoint: str
