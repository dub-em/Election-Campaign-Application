from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['Politicians Reputation']
)


list_of_politicians = ['PeterObi','Peter Obi','PO','AA','AtikuAbubakar',
                       'Atiku Abubakar','Bola Ahmed Tinubu','Bola Tinubu',
                       'BAT','Tinubu']
#Future version will have an endpoint that will display list of all public office holder, so that
#end-users will not have to guess how to input a public office holders name for a search.


@router.get("/politicians_reputation/filter", response_model=List[schemas.GeneralResponse])
def get_alltweets(filter: str):
    """An endpoint to retrieve all tweets in the database, filtered by a specified name given by the 
    end-user, which is checked against a list of public office holder to confirm if the given name
    is in fact a public office holder.
    
    Future version will likely modify the validation method to check the input against a database
    containing the public office holders details, which will either be populated manually of scraped
    automatically."""
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
    """An endpoint to count all tweets in the database, filtered by a specified name given by the 
    end-user."""
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

    #Future versions will cover citizen's sentiment analysis on each public office holder. 