jmjccgvcccccccccgvjxjcgjvcvccjgggccjgvvcjgggggvcjmcfrom pydantic import BaseModel

class paciente(BaseModel):
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


