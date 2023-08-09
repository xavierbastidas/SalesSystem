from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer, DECIMAL,CHAR,DATETIME, String
from Database.db import Base
import json
 
class VentaView(Base):
    __tablename__ = 'VentaView'
    idVenta =  Column(Integer,primary_key=True)
    numeroVenta = Column(CHAR(6))
    idCliente = Column(Integer)
    subTotal = Column(DECIMAL(10,2))
    impuestoTotal=Column(DECIMAL(10,2))
    Total=Column(DECIMAL(10,2))
    fechaRegistro=Column(DATETIME)
    nombre=Column(String(50))
    cedula=Column(String(10))
    telefono=Column(String(10))
    def __init__(self, idVenta, numeroVenta, 
                  idCliente, subTotal ,impuestoTotal,
                Total, fechaRegistro,nombre,
                cedula,telefono):
        self.idVenta = idVenta
        self.numeroVenta = numeroVenta
        self.idCliente = idCliente
        self.subTotal = subTotal
        self.impuestoTotal = impuestoTotal
        self.Total = Total
        self.fechaRegistro = fechaRegistro
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
    def __iter__(self):
        yield from {
            "idVenta": self.idVenta,
            "numeroVenta": self.numeroVenta,
            "idCliente": self.idCliente,
            "subTotal": str(self.subTotal),
            "impuestoTotal":str(self.impuestoTotal),
            "Total":str(self.Total),
            "fechaRegistro":str(self.fechaRegistro),
            "nombre":self.nombre,
            "cedula":self.cedula,
            "telefono":self.telefono       
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
    

class Venta(Base):
    __tablename__ = 'Venta'
    idVenta =  Column(Integer,primary_key=True)
    numeroVenta = Column(CHAR(6))
    idCliente = Column(Integer)
    subTotal = Column(DECIMAL(10,2))
    impuestoTotal=Column(DECIMAL(10,2))
    Total=Column(DECIMAL(10,2))
    fechaRegistro=Column(DATETIME)
    def __init__(self, idVenta, numeroVenta, 
                  idCliente, subTotal ,impuestoTotal,
                Total, fechaRegistro):
        self.idVenta = idVenta
        self.numeroVenta = numeroVenta
        self.idCliente = idCliente
        self.subTotal = subTotal
        self.impuestoTotal = impuestoTotal
        self.Total = Total
        self.fechaRegistro = fechaRegistro
    def __iter__(self):
        yield from {
            "idVenta": self.idVenta,
            "numeroVenta": self.numeroVenta,
            "idCliente": self.idCliente,
            "subTotal": str(self.subTotal),
            "impuestoTotal":str(self.impuestoTotal),
            "Total":str(self.Total),
            "fechaRegistro":str(self.fechaRegistro),    
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()




 
