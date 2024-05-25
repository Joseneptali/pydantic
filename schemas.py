from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class MedicoCreate(BaseModel):
    nombre: str
    apellido: str
    usuario: str
    email: str
    contraseña: str

class Medico(BaseModel):
    id: int
    nombre: str
    apellido: str
    usuario: str
    email: str

    class Config:
        orm_mode = True

class MedicoLogin(BaseModel):
    username: str
    password: str