#!/usr/bin/env python

import argparse
import sys

from src.helpers.Printer import Printer
from src.helpers.HelpStrings import HelpString

class Tweet(object):

    def __init__(self, twitter):
        parser = argparse.ArgumentParser(
            description=HelpString.get_tweet_string("tweet_description"),
            usage=HelpString.get_tweet_string("help_usage"),
        )
        parser.add_argument( "-m", action="store" , required=True, help=HelpString.get_tweet_string("arg_m"))
        args = parser.parse_args(sys.argv[2:])

        message = str(args.m)
        if self.isSuitableTweet(message) is False:
            print("Your tweet character limit is not suitable :: {length}".format(length=len(message)))
            exit(1)
        
        tweet = twitter.update_status(message)
        if tweet is not None:
            print("{username}::{created_at} -> {tweet}".format(username=tweet.user.name, created_at= tweet.created_at, tweet=tweet.text))
            exit(0)


    def isSuitableTweet(self,message):
        if len(message) > 140:
            return False

        return True

if __name__ == "__main__":
    Tweet()