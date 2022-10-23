# Election-Campaign-Application
This application will enable end-users to answer essential campaign and governance related question, using extracted, wrangled and analyzed data from the social media platform called Twitter.

### Election Database
+ This part/branch of the phase 1 was focused on creating and deploying an AWS Postgres Instance.
+ Pulling a week's worth of data from Twitter API (one of many intended sources of data that will be exploited in the subsequent phases of the project), and storing it on the remote Postgres database, so as to make the project less dependent of on the response time of the Twitter API.
+ Hosting a Script to update the database on a daily basis, and delete any data older than a week, as the intended focus period is a week.
