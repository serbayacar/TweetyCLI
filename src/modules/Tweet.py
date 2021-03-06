#!/usr/bin/env python

import os
import requests
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
        parser.add_argument( "--attach", action="store" , required=False, help=HelpString.get_tweet_string("arg_m"))
        args = parser.parse_args(sys.argv[2:])

        message = str(args.m)
        if self.isSuitableTweet(message) is False:
            print("Your tweet character limit is not suitable :: {length}".format(length=len(message)))
            exit(1)

        if args.attach is not None:
            image = self.getImage(args.attach)
            tweet = twitter.update_with_media(image, message)
            
            if os.path.exists('temp.jpg'):
                os.remove('temp.jpg')
        else:
            tweet = twitter.update_status(message)

        if tweet is not None:
            print("{username}::{created_at} -> {tweet}".format(username=tweet.user.name, created_at= tweet.created_at, tweet=tweet.text))
            exit(0)


    def isSuitableTweet(self,message):
        if len(message) > 140:
            return False

        return True

    def getImage(self, url):
        ### Import Regex Lib
        import re

        ### Regex applying
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        ### URL is from localhost
        if os.path.exists(url):
            url = url
        ### URL is from external website
        elif re.match(regex, url) is not None:
            filename = 'temp.jpg'
            request = requests.get(url, stream=True)
            if request.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in request:
                        image.write(chunk)

                    url = filename
            else:
                print("Unable to download image")
                exit(1)
        else:
            print("Give a valid URL, please.")
            exit(1)

        return url
                

if __name__ == "__main__":
    Tweet()