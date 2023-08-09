from sqlalchemy import  Column
from sqlalchemy.sql.sqltypes import Integer,String,DateTime,DECIMAL
from Database.db import Base
import json
 
class Producto(Base):
    __tablename__ = 'ProductoView'
    idProducto = Column(Integer,primary_key=True)
    marca= Column(String(50))
    descripcion = Column(String(100))
    idCategoria = Column(Integer)
    stock = Column(Integer)
    precio=Column(DECIMAL(10,2))
    fechaRegistro=Column(DateTime)
    categoria = Column(String(50))
    def __init__(self, idProducto, marca, descripcion, idCategoria, stock,precio,fechaRegistro,
                 categoria):
        self.idProducto = idProducto
        self.marca = marca
        self.descripcion=descripcion
        self.idCategoria = idCategoria
        self.stock=stock 
        self.precio = precio
        self.fechaRegistro= fechaRegistro
        self.categoria = categoria
    def __iter__(self):
        yield from {
            "idProducto": self.idProducto,
            "marca": self.marca,
            "descripcion": self.descripcion,
            "idCategoria": self.idCategoria,
            "stock": self.stock,
            "precio":str(self.precio),
            "fechaRegistro":str(self.fechaRegistro),
            "categoria":self.categoria
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

