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
    week_ago = datetime.date.today() - datetime.timedelta(days=1)
    yester = datetime.date.today() - datetime.timedelta(days=1)
    print(week_ago)

def email():
    import os
    import ssl
    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from typing import Any, cast, List

    from prefect import Task
    from prefect.client import Secret
    from prefect.utilities.tasks import defaults_from_attrs
    prefect.tasks.notifications.email_task.EmailTask.run(
        subject='TESTING', 
        msg='it works', 
        email_to='georgemichaeldagogo@gmail.com', 
        email_from=None, 
        smtp_server=None, 
        smtp_port=25, 
        smtp_type="INSECURE", 
        msg_plain=None, 
        email_to_cc=None, 
        email_to_bcc=None, 
        attachments=None)

email()