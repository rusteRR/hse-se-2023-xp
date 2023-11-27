from pydantic import BaseModel

class Hw(BaseModel):
    id  : int
    text: str