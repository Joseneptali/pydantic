from pydantic import BaseModel

class Cita(BaseModel):
  codigo_cita: int;
  nombre_paciente: int;
  especialidad: str;
  medico: str;
  fecha: str;
  tiempo: int;
  email: str;
  numero_telefono: str;
  mensaje: str
