from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['Politicians Reputation']
)

list_of_politicians = ['PeterObi','Peter Obi','PO','AA','AtikuAbubakar',
                       'Atiku Abubakar','Bola Ahmed Tinubu','Bola Tinubu',
                       'BAT','Tinubu']

@router.get("/politicians_reputation/filter", response_model=List[schemas.GeneralResponse])
def get_alltweets(filter: str):
    conn, cursor = database.database_connection()
    if filter in list_of_politicians:
        if filter == 'Peter Obi' or filter == 'PeterObi' or filter == 'PO':
            cursor.execute("""SELECT * FROM election
                           WHERE tweet LIKE '%PeterObi%' OR tweet LIKE '%Peter Obi%' or tweet LIKE '%PO%';""")
            tweets = cursor.fetchall()
            return tweets
        elif filter == 'AA' or filter == 'AtikuAbubakar' or filter == 'Atiku Abubakar':
            cursor.execute("""SELECT * FROM election
                           WHERE tweet LIKE '%AA%' OR tweet LIKE '%AtikuAbubakar%' or tweet LIKE '%Atiku Abubakar%';""")
            tweets = cursor.fetchall()
            return tweets
        elif filter == 'Bola Ahmed Tinubu' or filter == 'Bola Tinubu' or filter == 'Tinubu' or filter == 'BAT':
            cursor.execute("""SELECT * FROM election
                           WHERE tweet LIKE '%Bola Ahmed Tinubu%' OR tweet LIKE '%Bola Tinubu%' or tweet LIKE '%Tinubu%' or tweet LIKE '%BAT%';""")
            tweets = cursor.fetchall()
            return tweets
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"'{filter}' does not exist in the list of Politicians!")
    conn.close()


@router.get("/politicians_reputation/filter_count")
def count_alltweets(filter: str):
    conn, cursor = database.database_connection()
    if filter in list_of_politicians:
        if filter == 'Peter Obi' or filter == 'PeterObi' or filter == 'PO':
            cursor.execute("""SELECT COUNT(*) FROM election
                           WHERE tweet LIKE '%PeterObi%' OR tweet LIKE '%Peter Obi%' or tweet LIKE '%PO%';""")
            tweets = cursor.fetchone()
            return tweets
        elif filter == 'AA' or filter == 'AtikuAbubakar' or filter == 'Atiku Abubakar':
            cursor.execute("""SELECT COUNT(*) FROM election
                           WHERE tweet LIKE '%AA%' OR tweet LIKE '%AtikuAbubakar%' or tweet LIKE '%Atiku Abubakar%';""")
            tweets = cursor.fetchone()
            return tweets
        elif filter == 'Bola Ahmed Tinubu' or filter == 'Bola Tinubu' or filter == 'Tinubu' or filter == 'BAT':
            cursor.execute("""SELECT COUNT(*) FROM election
                           WHERE tweet LIKE '%Bola Ahmed Tinubu%' OR tweet LIKE '%Bola Tinubu%' or tweet LIKE '%Tinubu%' or tweet LIKE '%BAT%';""")
            tweets = cursor.fetchone()
            return tweets
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"'{filter}' does not exist in the list of Politicians!")
    conn.close() 