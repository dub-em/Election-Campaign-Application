from pydantic import BaseModel
import datetime

class GeneralResponse(BaseModel):
    time_created: datetime.datetime 
    tweet: str 
    loca_tion: str
