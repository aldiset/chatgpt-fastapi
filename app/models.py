import enum
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Date, Enum
from app.database import Base

class Role(enum.Enum):
    user = 'user'
    system = 'system'
    function = 'function'
    assistant = 'assistant'

class Users(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String, nullable=False)
    email= Column(String, unique=True)
    phone= Column(String)
    address= Column(String)
    password= Column(String)
    date_of_birth= Column(Date)
    created_at= Column(DateTime, default=datetime.now())

class Rooms(Base):
    __tablename__= 'rooms'
    id= Column(Integer, primary_key=True, autoincrement=True)
    created_at= Column(DateTime, default=datetime.now())

class Chats(Base):
    __tablename__= 'chats'
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id= Column(Integer, ForeignKey("users.id"))
    room_id=Column(Integer, ForeignKey("rooms.id"))
    message_id= Column(String)
    role = Column(String, default="user")
    content= Column(String)
    created_at= Column(DateTime, default=datetime.now())