from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int] = None
    usuario: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 0,
                "usuario": "<USUARIO>",
                "password": "<PASSWORD>"
            }
        }
