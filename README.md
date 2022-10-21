# Election-Campaign-TPL

### Purpose of the Package
+ This library serves as an extension of and for the election campaign API (https://research-questions-api.herokuapp.com/docs#/). It is intended to aid developers who decide to use the API in a python IDE for research work related to election campaign and governance.

### Features
+ Collection of Research Questions Focus Areas
    - general_trends
        - get_alltweets()
        - get_limitedtweets()
        - get_filteredtweets()
    - politicians_reputation
        - get_alltweets()
        - count_alltwets()
    - citizens_sentiment
    - complaints_areas

### Getting Started
The package can be found on pypi hence you can install it using pip

### Installation
```bash
pip install election_campaign 
```

### Usage
politicians_reputation
```python
>>> from election_campaign import general_trends
>>>
>>> #Retrieve Nigeria centered-tweets using the general_trends.get_alltweets() function
>>> alltweets = general_trends.get_alltweets(data_type='json')
>>>
>>> #Retrieve limited Nigeria centered-tweets using the general_trends.get_limitedtweets() function
>>> limitedtweets = general_trends.get_limitedtweets(limit=10, data_type='pandas.dataframe')
```

### Example
```python
>>> from election_campaign import politicians_reputation
>>>
>>> #Retrieve the number of tweets about a certain politician from Nigeria centered-tweets using the politicians_reputation.get_alltweets() function
>>> tweetcount = politicians_reputation.count_alltweets(filter='Atiku Abubakar', data_type='json')
>>> print(tweetcount)
>>>
>>> '{"count": 1049}'
>>>
>>> tweetcount = politicians_reputation.count_alltweets(filter='Peter Obi', data_type='json')
>>> print(tweetcount)
>>>
>>> '{"count": 21261}'
```

### Contribution
This Project is open to contribution and collaboration. 
Feel free to connect.

### Author
+ Main Maintainer: Michael Dubem Igbomezie
