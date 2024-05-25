from pydantic import BaseModel

class cita(BaseModel):
  codigo_cita: int;
  nombre_paciente: str;
  especialidad: str;
  medico: str;
  fecha: str;
  tiempo: int;
  email: str;
  numero_telefono: int;
  mensaje: str;
