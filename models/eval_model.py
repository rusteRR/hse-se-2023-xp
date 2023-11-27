from pydantic import BaseModel

class Eval(BaseModel):
    hw_id  : int
    mark   : float
    comment: str
