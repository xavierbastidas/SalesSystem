from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer,String,DateTime
from Database.db import Base
import json
 
class Cliente(Base):
    __tablename__ = 'Cliente'
    idCliente = Column(Integer,primary_key=True)
    nombre = Column(String(50))
    cedula = Column(String(10))
    correo = Column(String(50))
    telefono = Column(String(10))
    fechaRegistro=Column(DateTime)
    def __init__(self, idCliente, nombre, cedula, correo, telefono,fechaRegistro):
        self.idCliente = idCliente
        self.nombre = nombre
        self.cedula=cedula
        self.correo = correo
        self.telefono= telefono
        self.fechaRegistro= fechaRegistro
    def __iter__(self):
        yield from {
            "idCliente": self.idCliente,
            "nombre": self.nombre,
            "cedula": self.cedula,
            "correo": self.correo,
            "telefono": self.telefono,
            "fechaRegistro":str(self.fechaRegistro)
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()




 


 
 