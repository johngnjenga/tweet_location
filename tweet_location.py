import os
import tweepy as tw
import pandas as pd
##
consumer_key= 'Use your consumer_key'
consumer_secret= 'Use your consumer_secret'
access_token= 'Use your access_token'
access_token_secret= 'Use your access_token_secret'
##
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
##
# Define the search term and the date_since date as variables
import datetime
x = "2021-5-7"
search_words = "deep state"
date_since =x
##
# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets
##
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
    ##
    # Collect tweets
tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="en",
                       since=date_since).items(1)

# Collect a list of tweets
[tweet.text for tweet in tweets]
##
new_search = search_words + " -filter:retweets"
new_search
##
tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(5)

[tweet.text for tweet in tweets]
##
tweets = tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(100)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs