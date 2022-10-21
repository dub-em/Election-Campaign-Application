try:
    import pandas
    import json
    import requests
except:
    print("Please install (pip install) and import the following python library (pandas, json, requests).")

url = "https://research-questions-api.herokuapp.com/politicians_reputation/"

def get_alltweets(filter=None, data_type=None):
    """An endpoint to retrieve all tweets in the database, filtering the result by tweets using
    whichever name of a public office holder specified by the end-user.

    Parameters
    ----------
    filter: str
        The string (keyword) specified by the end user to filter the result of the query by tweets.
    data_type : None, "json" or "pandas.dataframe"
        The preferred data type of the result of the api request, as specified by the end user.

    Returns
    -------
    data
        The filtered result of the api request in the data format specified by the end user.
    """
    
    if filter == None:
        return ("Please specify an string (keyword) for the filter!")
    elif type(filter) == str:
        url_temp = url + "filter?filter=" + filter
        request = requests.get(url = url_temp)
        data = request.json()
        data = json.dumps(data)
        
        if (data_type == None) or (data_type == "json"):
            return data
        elif data_type == "pandas.dataframe":
            data = pandas.read_json(data)
            return data
        else:
            return ("Incorrect or unavailable specified data type!")
    else:
        return ("Please specify an string (keyword) for the filter!")

    
def count_alltweets(filter=None, data_type=None):
    """An endpoint to count all tweets in the database, filtering the result by tweets using
    whichever name of a public office holder specified by the end-user.

    Parameters
    ----------
    filter: str
        The string (keyword) specified by the end user to filter the result of the query by tweets.
    data_type : None, "json" or "pandas.dataframe"
        The preferred data type of the result of the api request, as specified by the end user.

    Returns
    -------
    data
        The filtered result of the api request in the data format specified by the end user.
    """
    
    if filter == None:
        return ("Please specify an string (keyword) for the filter!")
    elif type(filter) == str:
        url_temp = url + "filter_count?filter=" + filter
        request = requests.get(url = url_temp)
        data = request.json()
        data = json.dumps(data)
        
        if (data_type == None) or (data_type == "json"):
            return data
        elif data_type == "pandas.dataframe":
            data = pandas.read_json(data)
            return data
        else:
            return ("Incorrect or unavailable specified data type!")
    else:
        return ("Please specify an string (keyword) for the filter!")