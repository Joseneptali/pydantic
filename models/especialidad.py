from pydantic import BaseModel

class Especialidad(BaseModel):
   id: int,
   especialidad: str,
   descripcion: str,
   estado: str
