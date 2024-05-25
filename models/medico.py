from pydantic import BaseModel
from core.config import Base

class Medico(BaseModel):
   nombre: str
   apellido: str
   usuario: str
   email: str
   contrasena: str
   fecha_nacimiento: str
   sexo: str
   direccion: str
   pais: str
   ciudad: str
   codigo_postal: str
   telefono: str
   estado: str
