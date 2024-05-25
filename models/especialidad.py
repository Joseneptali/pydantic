from pydantic import BaseModel

class especialidad(BaseModel):
   codigo_especialidad: int;
   nombre_especialidad: str;
   descripcion: str;
   estado: str;
