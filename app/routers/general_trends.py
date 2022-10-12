from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['General Trends']
)

cursor = database.cursor
conn = database.conn

#@router.get("/posts", response_model=List[schemas.PostResponse])
#def get_posts(limit: int = 2):
    #cursor.execute("""SELECT * FROM posts LIMIT %s""",(str(limit)))
    #posts = cursor.fetchall()
    #return posts