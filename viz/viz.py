import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re  
import spacy
#nlp = spacy.load('en_core_web_lg')

import tweepy
import configparser
import pandas as pd
import psycopg2
from datetime import date
import datetime 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

config = configparser.ConfigParser()
config.read("config.ini")

today = datetime.date.today()
week_ago = datetime.date.today() - datetime.timedelta(days=4)
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
limit = 100

tweets = tweepy.Cursor(api.search_tweets, q = keywords,count = 200, tweet_mode = 'extended',geocode='9.0820,8.6753,450mi', until=yester).items(limit)

columns = ['time_created', 'screen_name','name', 'tweet','loca_tion', 'descrip_tion','verified','followers', 'source','geo_enabled','retweet_count','truncated','lang','likes']
data = []


for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.user.name,tweet.full_text, tweet.user.location, tweet.user.description,tweet.user.verified,tweet.user.followers_count,tweet.source,tweet.user.geo_enabled,tweet.retweet_count,tweet.truncated,tweet.lang,tweet.favorite_count])
    
df = pd.DataFrame(data , columns=columns)
df = df[~df.tweet.str.contains("RT")]
#removes retweeted tweets
df = df.reset_index(drop = True)

df = df.tweet

all_sentences = []

for word in df:
    all_sentences.append(word)

all_sentences
#df1 = df.to_string()

#df_split = df1.split()

#df_split
lines = list()
for line in all_sentences:    
    words = line.split()
    for w in words: 
       lines.append(w)


#Removing Punctuation

lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]


lines2 = []

for word in lines:
    if word != '':
        lines2.append(word)


# ...
lines3 = [word for word in lines2 if word not in stopwords.words('english')]

lines4 = [i for i in lines3 if len(i) >= 2]

df1 = pd.DataFrame(lines4, columns= ['words'])
df2 = df1.value_counts()
df3 = (df2.head(10))
plt.figure(figsize=(10,5))
sns.barplot(df3.values, df3.index, alpha=0.8)
plt.title('Top Organizations Mentioned')
plt.ylabel('Word from Tweet', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()