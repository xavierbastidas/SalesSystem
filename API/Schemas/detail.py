from pydantic import BaseModel 
from decimal import Decimal
class Detail(BaseModel):
    idDetalleVenta:int | None = None
    idProducto:int
    marcaProducto:str
    descripcionProducto:str
    categoriaProducto:str
    cantidad:int
    precio:Decimal
    total:Decimal
    idVenta:int|None = None
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

