from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String)
    password = Column(String)
    role = Column(Integer)
    public_key = Column(String)
    remark = Column(String)