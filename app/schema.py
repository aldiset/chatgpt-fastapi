from typing import List
from pydantic import BaseModel

class SchemaChats(BaseModel):
    role: str
    content: str