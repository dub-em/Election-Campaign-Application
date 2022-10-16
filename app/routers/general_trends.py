from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['General Trends']
)

cursor = database.cursor
conn = database.conn

@router.get("/generaltrends", response_model=List[schemas.GeneralResponse])
def get_alltweets():
    cursor.execute("""SELECT * FROM election""")
    tweets = cursor.fetchall()
    return tweets

@router.get("/generaltrends/limit", response_model=List[schemas.GeneralResponse])
def get_limitedtweets(limit: int):
    cursor.execute("""SELECT * FROM election LIMIT {}""".format(str(limit)))
    tweets = cursor.fetchall()
    return tweets

@router.get("/generaltrends/filter", response_model=List[schemas.GeneralResponse])
def get_filteredtweets(filter: str):
    cursor.execute("""SELECT * FROM election WHERE tweet LIKE '%{}%';""".format(filter))
    tweets = cursor.fetchall()
    return tweets