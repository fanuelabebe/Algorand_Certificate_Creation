from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI();

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,

)

class AccountBase(BaseModel):
    user_name: str
    password: str
    role: int
    public_key: str
    remark: str

class AccountModel(AccountBase):
    id:int

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/accounts/",response_model=AccountModel)
async def create_account(account:AccountBase,db:db_dependency):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@app.get("/accounts/",response_model=List[AccountModel])
async def read_accounts(db:db_dependency,skip:int = 0,limit: int = 100):
    accounts = db.query(models.Account).offset(skip).limit(limit).all()
    return accounts