from fastapi import APIRouter ,Depends , status , HTTPException
from Database.db import  get_db  
from Database.server_time import return_server_time
from Models.customer import Cliente
from Schemas.customer import Customer
from sqlalchemy.orm import Session
import json
router = APIRouter(prefix="/customers",tags=["customers"])
 
@router.get("/",status_code=status.HTTP_200_OK)
def get_customers(db:Session=Depends(get_db)):
     try:
        data=  db.query(Cliente).all()
        if (len(data)==0):
            return {"codigo":status.HTTP_404_NOT_FOUND,
                "message": "data not found"}
        return json.loads(data.__str__())
     except HTTPException as ex:
          return {"error": ex.args.__str__()}

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_customers(customer:Customer,db:Session=Depends(get_db)):
     try:
        new_customer = Cliente(**customer.model_dump())
        new_customer.fechaRegistro =  return_server_time()
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return json.loads(new_customer.__str__())
     except HTTPException as ex:
         return {"error":ex.args.__str__()}
         
    

     





    

