from fastapi import APIRouter ,Depends , status ,HTTPException
from Database.db import  get_db  , conn 
from Models.detail import DetalleVenta 
from Schemas.detail import Detail 
from sqlalchemy.orm import Session 
from Database.query import insert_detail, create_values_detail , return_lasted_detail
import json
router = APIRouter(prefix="/detail",tags=["detail"])
@router.get("/{idVenta}",status_code=status.HTTP_200_OK)
def get_details(idVenta:int,db:Session=Depends(get_db)):
     try:
        data=  db.query(DetalleVenta).where(DetalleVenta.idVenta==idVenta).all()
        if len(data)==0:
              return {"codigo":status.HTTP_404_NOT_FOUND,
                "message": "data not found"}
        return json.loads(data.__str__())
     except HTTPException as ex:
          return {"error":ex.args.__str__()}

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_details(detail:Detail,db:Session=Depends(get_db)):
     try:
        values = create_values_detail(detail,db)
        conn.execute(insert_detail,values)
        conn.commit()
        return return_lasted_detail(db)
     except HTTPException as ex:
         return {"error": ex.args.__str__()}

