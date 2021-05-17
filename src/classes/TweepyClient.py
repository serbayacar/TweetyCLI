#!/usr/bin/env python

import tweepy
from src.helpers.ConfigParser import Config

class TweepyClient():

    consumer_key = Config().getConfig("CONSUMER_KEY") 
    consumer_secret = Config().getConfig("CONSUMER_SECRET") 
    access_token = Config().getConfig("ACCESS_TOKEN") 
    access_secret = Config().getConfig("ACCESS_SECRET") 
    client = False

    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        try:
            self.client = tweepy.API(auth)
            self.client.verify_credentials()

            # print("Authentication OK")
        except:
            print("Error during authentication")
            exit(0)


    def getClient(self):
        return self.client

    def getTweets(self):
        tweets = self.client.home_timeline()  
        return tweets