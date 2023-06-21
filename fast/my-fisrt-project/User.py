from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    phone: float
    lastname: Optional[str]
