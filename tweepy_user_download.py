# -*- coding: utf-8 -*-
import tweepy

# twitter for developer keys
api_key = ''
api_secret_key = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

# start API access
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# get tweet from profile using screen_name ('user' portion of '@user')
screen_name = ''

# collects in batches of 100 due to rate limit issues, see API documentation
n_tweets = 100
tweets_json = []
new_tweets = api.user_timeline(screen_name=screen_name, count=n_tweets, tweet_mode='extended')
tweets_json += [tweet._json for tweet in new_tweets]

# report download amount
print(len(tweets_json), ' downloaded', end='\t')
# get last id
lastid = tweets_json[-1]['id']
print(lastid, ' max_id')

while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=screen_name, count=n_tweets, max_id=lastid, tweet_mode='extended')
    tweets_json += [tweet._json for tweet in new_tweets]
    lastid = tweets_json[-1]['id'] - 1

    print(len(tweets_json), ' downloaded', end='\t')
    print(lastid, ' max_id')

import json
import os

path = './'
file = screen_name + '_tweets.json'
save = os.path.join(path, file)

with open(save, 'w') as outfile:
    json.dump(tweets_json, outfile)

with open(save) as infile:
    data = json.load(infile)
len(data)
