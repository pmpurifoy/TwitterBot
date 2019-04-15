import sched, time
import config
import tweepy
import json
from tweepy.auth import OAuthHandler

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
s = sched.scheduler(time.time, time.sleep)
numberOfTweets = 1
def do_something(sc):
    global numberOfTweets
    try:
        #api.update_status("@" + username + ' Harden is the best.', in_reply_to_status_id = tweet.id)
        message = str(numberOfTweets) + '. James Harden is the MVP'
        api.update_status(message)
    except tweepy.TweepError as e:
       print(e.reason)
    numberOfTweets+=1
    s.enter(43200, 1, do_something, (sc,))

s.enter(0, 1, do_something, (s,))
s.run()
