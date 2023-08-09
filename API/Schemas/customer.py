from pydantic import BaseModel 
from datetime import datetime
class Customer(BaseModel):
    idCliente:int | None = None
    nombre:str
    cedula:str
    correo:str
    telefono:str
    fechaRegistro:datetime|None =None
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


