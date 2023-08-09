from  fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from Routes import customer , product , detail , sell
app= FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                    allow_credentials=True,
                     allow_methods=["*"],
                    allow_headers=["*"]
                   )
app.include_router(customer.router)
app.include_router(product.router)
app.include_router(detail.router)
app.include_router(sell.router)
print("http://localhost:8000")
@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}














  


