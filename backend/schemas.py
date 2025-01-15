from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class LinkCreate(BaseModel):
    name_start : str
    direction : str
    relation : str
    quantor : str
    name_end : str 
    ring : int

# Complete ToDo Schema (Pydantic Model)
class Link(BaseModel):
    id : int
    name_start : str
    direction : str
    relation : str
    quantor : str
    name_end : str 
    ring : int

    class Config:
        orm_mode = True

class RuleCreate(BaseModel):
    directions : str
    relations : str
    quantors : str
    res_direction : str
    res_relation : str
    res_quantor : str

class Rule(BaseModel):
    id :  int
    directions : str
    relations : str
    quantors : str
    res_direction : str
    res_relation : str
    res_quantor : str

    class Config:
        orm_mode = True