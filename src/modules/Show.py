#!/usr/bin/env python

import argparse
import sys

from src.helpers.Printer import Printer
from src.helpers.HelpStrings import HelpString

class Show(object):

    def __init__(self, twitter):
        parser = argparse.ArgumentParser(
            description=HelpString.get_show_string("show_description"),
            usage=HelpString.get_show_string("help_usage"),
        )
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument("-m", "--me", action="store_true", help=HelpString.get_show_string("arg_me"))
        group.add_argument("-u", "--user", action="store", help=HelpString.get_show_string("arg_username"))
        parser.add_argument("-c", "--count", action="store", type=int , default=20, help=HelpString.get_show_string("arg_count"))
        args = parser.parse_args(sys.argv[2:])

        ## Get tweets from Twitter
        tweets = None
        if args.me is True:
            tweets = twitter.user_timeline('serbayacar', count=int(args.count))

        if args.user is not None:
            tweets = twitter.user_timeline(args.user,count=int(args.count))

        if tweets is None:
            tweets = twitter.home_timeline(count=int(args.count))

        ### Printing out tweets as a table        
        printer = Printer()
        table = printer.asTable('Timeline Tweets')
        table = printer.addColumn(table, ["User","Tweets"])

        for tweet in tweets:
            table = printer.addRow(table, tweet)

        table = printer.print(table)


if __name__ == "__main__":
    Show()