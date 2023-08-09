from fastapi import APIRouter ,Depends , status , HTTPException
from Database.db import  get_db 
from Models.product import Producto
from sqlalchemy.orm import Session
import json
router = APIRouter(prefix="/products",tags=["products"])
 
@router.get("/",status_code=status.HTTP_200_OK)
def get_products(db:Session=Depends(get_db)):
     try:
        data=  db.query(Producto).where(Producto.stock>0).all()
        if (len(data)==0):
               return {"codigo":status.HTTP_404_NOT_FOUND,
                "message": "data not found"}
        return json.loads(data.__str__())
     except HTTPException as ex:
          return {"error": ex.args.__str__()}





