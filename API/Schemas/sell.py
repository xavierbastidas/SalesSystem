from pydantic import BaseModel 
from decimal import Decimal
from datetime import datetime
class Sell(BaseModel):
    idVenta:int | None = None
    numeroVenta:str
    idCliente:int
    subTotal:Decimal
    impuestoTotal:Decimal
    Total:Decimal
    fechaRegistro:datetime
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

