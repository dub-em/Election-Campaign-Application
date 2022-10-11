import tweepy
import configparser
import pandas as pd
import psycopg2
from datetime import date
import datetime 


today = datetime.date.today()
week_ago = datetime.date.today() - datetime.timedelta(days=7)
yester = datetime.date.today() - datetime.timedelta(days=1)
print(yester)

config = configparser.ConfigParser()
config.read("config.ini")


def get_data():
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
    limit = 1000000

    tweets = tweepy.Cursor(api.search_tweets, q = keywords,count = 200, tweet_mode = 'extended',geocode='9.0820,8.6753,450mi', until=week_ago).items(limit)

    columns = ['time_created', 'screen_name','name', 'tweet','loca_tion', 'descrip_tion','verified','followers', 'source','geo_enabled','retweet_count','truncated','lang','likes']
    data = []


    for tweet in tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.user.name,tweet.full_text, tweet.user.location, tweet.user.description,tweet.user.verified,tweet.user.followers_count,tweet.source,tweet.user.geo_enabled,tweet.retweet_count,tweet.truncated,tweet.lang,tweet.favorite_count])
        
    df = pd.DataFrame(data , columns=columns)
    df = df[~df.tweet.str.contains("RT")]
    #removes retweeted tweets
    df = df.reset_index(drop = True)

    df.to_csv('tweets.csv')
    
    sf = pd.read_csv('tweets.csv')
    sf = sf.drop(sf.columns[0],axis = 1) #remove unnamed column sf[0]
    
    #sf.tweet = sf.tweet.str.replace(r'\W'," ")#replace all non aphabetic characters with space
    #sf.descrip_tion = sf.descrip_tion.str.replace(r'\W'," ")
    

    sf.to_csv(r'tweets.csv', index = False, header=True) #save to same csv file


def postgre_push():
    conn = psycopg2.connect(database="test",
                            user='postgres', password='george9042',
                            host='127.0.0.1', port='5433'
    )

    conn.autocommit = True
    cursor = conn.cursor()


    sql = ''' CREATE TABLE IF NOT EXISTS election_tweets
            (    name varchar(100) NOT NULL,
                time_created timestamp,
                screen_name varchar(100),
                tweet varchar(4000),
                loca_tion varchar(200),
                descrip_tion varchar,
                verified varchar(10) NOT NULL,
                followers int,
                source varchar(50),
                geo_enabled varchar(10) NOT NULL,
                retweet_count int,
                truncated varchar(10) NOT NULL,
                lang varchar(10),
                likes varchar(10) NOT NULL
            ) 
        '''


    cursor.execute(sql)

    sql2 = '''COPY election_tweets(time_created,screen_name,name,tweet,loca_tion,descrip_tion,verified,followers,source,geo_enabled,retweet_count,truncated,lang,likes)
    FROM 'C:/Users/HP/Downloads/Primis/tweets.csv' DELIMITER ',' CSV HEADER;''' 

    cursor.execute(sql2)

   # sql3 = '''select * from election;'''
    #cursor.execute(sql3)
    #for i in cursor.fetchall():
     #   print(i)

    conn.commit()
    conn.close()