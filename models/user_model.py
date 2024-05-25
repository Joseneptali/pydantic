from core.config import Base
import mysql.connector
from sqlalchemy import Column, Integer, String


class Medico(Base):
    __tablename__ = 'medicos'

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True, index=True)
    password = Column(String)
