import json

import tweepy

# Twitter credentials
with open('plugins/Qtwitter/tokens.json') as tokens_file:
    tokens = json.load(tokens_file)

CONSUMER_KEY = tokens['CONSUMER_KEY']
CONSUMER_SECRET = tokens['CONSUMER_SECRET']
ACCESS_KEY = tokens['ACCESS_KEY']
ACCESS_SECRET = tokens['ACCESS_SECRET']

# Set Twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Start Twitter API
api = tweepy.API(auth)
print('Api ok!')

def test():
    print('test!!')

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print('*'*80)

class MyOtherStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print('$'*80)

myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myOtherStream = tweepy.Stream(auth = api.auth, listener=MyOtherStreamListener())

myStream.filter(track=['opensource'], async=True)
myOtherStream.filter(track=['gif'], async=True)
