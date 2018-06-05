import tweepy
from auth import get_api     #from auth page import the get_api function.

api = get_api()

# enter a topic and return the info for number of tweets.
def search(query,count): 
    return [status for status in tweepy. Cursor(api.search, q = query).items(count)] #tweepys cursor is a prebuilt search feature made to use q = query for searching.

tweets = (search("#kanye",10))     # topic, amount of tweets.


for tweet in tweets:        # for each tweet print out the text.
    print(tweet.text)


