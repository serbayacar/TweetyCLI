#!/usr/bin/env python

# import argparse
# import sys

from src.helpers.Printer import Printer
# from src.helpers.HelpStrings import HelpString

class Show(object):
    twitter = None

    def __init__(self,twitter):
        printer = Printer()
        table = printer.asTable('Timeline Tweets')
        table = printer.addColumn(table, ["User","Tweets"])

        tweets = twitter.getTweets()
        for tweet in tweets:
            table = printer.addRow(table, tweet)

        table = printer.print(table)


if __name__ == "__main__":
    Show()