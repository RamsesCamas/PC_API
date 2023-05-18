from pydantic import BaseModel

class CPU(BaseModel):
    name:str
    price:int