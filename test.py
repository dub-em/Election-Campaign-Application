def test1():
    conn = psycopg2.connect(database="test",
                                user='postgres', password='george9042',
                                host='127.0.0.1', port='5433'
        )
    conn.autocommit = True
    cursor = conn.cursor()




    sql2 = '''COPY election_tweets(time_created,screen_name,name,tweet,loca_tion,descrip_tion,verified,followers,source,geo_enabled,retweet_count,truncated,lang,likes)
    FROM 'C:/Users/HP/Downloads/Primis/tweets.csv' DELIMITER ',' CSV HEADER;''' 

    cursor.execute(sql2)

    sql3 = '''DELETE FROM election_tweets WHERE time_created < current_timestamp - interval '7' day;'''

    cursor.execute(sql3)



    conn.commit()
    conn.close()

def time():
    from datetime import date
    import datetime
    today = datetime.date.today()
    week_ago = datetime.date.today() - datetime.timedelta(days=4)
    yester = datetime.date.today() - datetime.timedelta(days=1)
    print(week_ago)

time()