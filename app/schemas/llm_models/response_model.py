from pydantic import BaseModel


class ResponseSchema(BaseModel):
    review: str
