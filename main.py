import os
import openai
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from app.models import Chats, Users, Rooms
from app.crud import CRUDManager
from app.schema import SchemaChats
from app.database import SessionLocal

app = FastAPI()
crud_chat = CRUDManager(Chats)
crud_user = CRUDManager(Users)
crud_room = CRUDManager(Rooms)

# Initialize your OpenAI API key
openai.api_key = os.getenv("API_KEY_CHAT_GPT") #add api key in env config

@app.post("/chat/{room_id}")
async def chat(chats: List[SchemaChats], room_id: int):

    
    with SessionLocal() as db:
        room = await crud_room.get_by_id(db=db, id=id)
        if not room:
            return HTTPException(status_code=404, detail="room id not found")
        # Send the health data as input to Chat GPT from OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change the model to match your needs
            messages=jsonable_encoder(chats)
        )
        message_gpt = {
            "room_id": room_id,
            "message_id":response.get("id"),
            "role":response.get("choices")[0].get("message").get("role"),
            "content":response.get("choices")[0].get("message").get("content")
        }

        user_message = jsonable_encoder(chats[-1])
        user_message["room_id"]=room_id

        await crud_chat.create(db=db, data=user_message)
        await crud_chat.create(db=db, data=message_gpt)
    
    return response

@app.post("/room")
async def room():
    with SessionLocal() as db:
        return await crud_room.create(db=db, data={})
