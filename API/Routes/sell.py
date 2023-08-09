from fastapi import APIRouter ,Depends , status , HTTPException
from Database.db import  get_db 
from Database.server_time import return_server_time
from Models.sell import VentaView , Venta
from Schemas.sell import Sell
from sqlalchemy.orm import Session
import json
router = APIRouter(tags=["sell"])

@router.get("/sales",status_code=status.HTTP_200_OK)
def get_sell(db:Session=Depends(get_db)):
     try:
        data=  db.query(VentaView).all()
        if len(data)==0:
              return {"codigo":status.HTTP_404_NOT_FOUND,
                "message": "data not found"}
        return json.loads(data.__str__())
     except HTTPException as ex:
          return {"error":ex.args.__str__()}

@router.post("/sell",status_code=status.HTTP_201_CREATED)
async def create_sell(sell:Sell,db:Session=Depends(get_db)):
     try:
        new_sell = Venta(**sell.model_dump())
        new_sell.fechaRegistro = await return_server_time()
        db.add(new_sell)
        db.commit()
        db.refresh(new_sell)
        return json.loads(new_sell.__str__())
     except HTTPException as ex:
         return {"error":ex.args.__str__() }
     

