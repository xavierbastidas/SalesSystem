from sqlalchemy import  text
from Schemas.detail import Detail
from sqlalchemy.orm import Session
from Models.sell import Venta
from Models.detail import DetalleVenta
from sqlalchemy import desc
from fastapi import Depends
from Database.db import get_db

insert_detail = text("INSERT INTO DetalleVenta (idProducto, marcaProducto, descripcionProducto, categoriaProducto, cantidad, precio, total,idVenta) "
           "VALUES (:idProducto, :marcaProducto, :descripcionProducto, :categoriaProducto, :cantidad, :precio, :total ,:idVenta)")

def create_values_detail(detail:Detail ,db:Session=Depends(get_db())):
    latest_id_venta = db.query(Venta.idVenta).order_by(desc(Venta.idVenta)).limit(1).scalar()
    values = {
        'idProducto': detail.idProducto,
        'marcaProducto': detail.marcaProducto,
        'descripcionProducto': detail.descripcionProducto,
        'categoriaProducto': detail.categoriaProducto,
        'cantidad': detail.cantidad,
        'precio': detail.precio,
        'total': detail.total,
        'idVenta': latest_id_venta
         }
    return values 

def return_lasted_detail(db: Session = Depends(get_db())):
    lasted_detail = db.query(DetalleVenta).order_by(desc(DetalleVenta.idDetalleVenta)).first()
    return lasted_detail


 