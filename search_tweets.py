import tweepy
from auth import get_api     #from auth page import the get_api function.

api = get_api()

# enter a topic and return the info for number of tweets.
def search(query,count): 
    return [{'id': status.id, 'text': status.text} for status in tweepy. Cursor(api.search, q = query).items(count)] #tweepys cursor is a prebuilt search feature made to use q = query for searching.




