conn = psycopg2.connect(database="test",
                            user='postgres', password='george9042',
                            host='127.0.0.1', port='5433'
    )
conn.autocommit = True
cursor = conn.cursor()




sql2 = '''COPY election(time_created,screen_name,name,tweet,loca_tion,descrip_tion,verified,followers,source,geo_enabled,retweet_count,truncated,lang,likes)
FROM 'C:/Users/HP/Downloads/Primis/tweets.csv' DELIMITER ',' CSV HEADER;''' 

cursor.execute(sql2)

sql3 = '''select * from election;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()