import tweepy
import configparser
import pandas as pd
import psycopg2
from datetime import date
import datetime 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read("config.ini")

today = datetime.date.today()
yester = datetime.date.today() - datetime.timedelta(days=1)

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

keywords = ['Buhari OR APC OR  PeterObi OR Tinubu OR PDP OR Atiku OR LabourParty']
#keywords = ['Buhari','APC', 'PeterObi','Tinubu','Atiku']
#it seems the api does not return every tweet containing at least one or every keyword, it returns the only tweets that contains every keyword
#solution was to use the OR in the keywords string as this is for tweets search only and might give errors in pure python
limit = 10000

tweets = tweepy.Cursor(api.search_tweets, q = keywords,count = 200, tweet_mode = 'extended',geocode='9.0820,8.6753,450mi', until=yester).items(limit)

columns = ['time_created', 'screen_name','name', 'tweet','loca_tion', 'descrip_tion','verified','followers', 'source','geo_enabled','retweet_count','truncated','lang','likes']
data = []


for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.user.name,tweet.full_text, tweet.user.location, tweet.user.description,tweet.user.verified,tweet.user.followers_count,tweet.source,tweet.user.geo_enabled,tweet.retweet_count,tweet.truncated,tweet.lang,tweet.favorite_count])
    
df = pd.DataFrame(data , columns=columns)
df = df[~df.tweet.str.contains("RT")]
#removes retweeted tweets
df = df.reset_index(drop = True)
print(df.time_created)


conn_string = 'postgresql://myadmin:electionapi@dubem-postgres.carjb4cqbkhg.us-east-2.rds.amazonaws.com:5432/postgres'
  
db = create_engine(conn_string)
conn = db.connect()

df.to_sql('election', con=conn, if_exists='append',
          index=False)
conn = psycopg2.connect(database="postgres",
                            user='myadmin', password='electionapi',
                            host='dubem-postgres.carjb4cqbkhg.us-east-2.rds.amazonaws.com', port='5432'
    )
conn.autocommit = True
cursor = conn.cursor()
  
sql1 = '''select * from election;'''
cursor.execute(sql1)

for i in cursor.fetchall():
    print(i)
  

sql2 = '''DELETE FROM election_tweets WHERE time_created < current_timestamp - interval '7' day;'''

cursor.execute(sql2)
conn.close()

#2022-10-09 done
#2022-10-08 done
