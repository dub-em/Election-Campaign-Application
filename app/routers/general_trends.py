from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['General Trends']
)

@router.get("/generaltrends", response_model=List[schemas.GeneralResponse])
def get_alltweets():
    conn, cursor = database.database_connection()
    cursor.execute("""SELECT * FROM election""")
    tweets = cursor.fetchall()
    conn.close()
    return tweets

@router.get("/generaltrends/limit", response_model=List[schemas.GeneralResponse])
def get_limitedtweets(limit: int):
    conn, cursor = database.database_connection()
    cursor.execute("""SELECT * FROM election LIMIT {}""".format(str(limit)))
    tweets = cursor.fetchall()
    conn.close()
    return tweets

@router.get("/generaltrends/filter", response_model=List[schemas.GeneralResponse])
def get_filteredtweets(filter: str):
    conn, cursor = database.database_connection()
    cursor.execute("""SELECT * FROM election WHERE tweet LIKE '%{}%';""".format(filter))
    tweets = cursor.fetchall()
    conn.close()
    return tweets