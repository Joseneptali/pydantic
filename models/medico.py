from pydantic import BaseModel

class medico(BaseModel):
   id: int,
   nombre: str,
   apellido: str,
   usuario: str,
   email: str,
   contrasena: str,
   fecha_nacimiento: str,
   sexo: int,
   direccion:  str,
   pais: str,
   ciudad: str,
   codigo_postal: str,
   telefono: str,
   estado: str
