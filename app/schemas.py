from pydantic import BaseModel, EmailStr
import datetime

class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True
