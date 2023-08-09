from sqlalchemy import  Column  
from sqlalchemy.sql.sqltypes import Integer,String,DECIMAL
from Database.db import Base 
import json
class DetalleVenta(Base):
    __tablename__ = 'DetalleVenta'
    idDetalleVenta = Column(Integer,primary_key=True)
    idVenta = Column(Integer)
    idProducto = Column(Integer)
    marcaProducto = Column(String(100))
    descripcionProducto = Column(String(100))
    categoriaProducto=Column(String(100))
    cantidad=Column(Integer)
    precio=Column(DECIMAL(10,2))
    total=Column(DECIMAL(10,2))
    def __init__(self,idDetalleVenta,idVenta, idProducto, 
                  marcaProducto, descripcionProducto,categoriaProducto,
                 cantidad, precio,total):
        self.idDetalleVenta = idDetalleVenta
        self.idVenta = idVenta
        self.idProducto = idProducto
        self.marcaProducto = marcaProducto
        self.descripcionProducto = descripcionProducto
        self.categoriaProducto = categoriaProducto
        self.cantidad = cantidad
        self.precio = precio
        self.total = total
    def __iter__(self):
        yield from {
            "idDetalleVenta":self.idDetalleVenta,
            "idVenta": self.idVenta,
            "idProducto": self.idProducto,
            "marcaProducto": self.marcaProducto,
            "descripcionProducto": self.descripcionProducto,
            "categoriaProducto":self.categoriaProducto,
            "cantidad":self.cantidad,
            "precio":str(self.precio),
            "total":str(self.total)
            
        }.items()
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)
    def __repr__(self):
        return self.__str__()




 


 
 