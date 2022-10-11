conn = psycopg2.connect(database="test",
                            user='postgres', password='george9042',
                            host='127.0.0.1', port='5433'
    )
conn.autocommit = True
cursor = conn.cursor()




sql2 = '''COPY election_tweets(time_created,screen_name,name,tweet,loca_tion,descrip_tion,verified,followers,source,geo_enabled,retweet_count,truncated,lang,likes)
FROM 'C:/Users/HP/Downloads/Primis/tweets.csv' DELIMITER ',' CSV HEADER;''' 

cursor.execute(sql2)

sql3 = '''DELETE FROM election_tweets WHERE timestamp < (NOW() - INTERVAL 7 DAY)'''
cursor.execute(sql3)


sql4 = ''' SELECT * FROM election_tweets;'''
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()