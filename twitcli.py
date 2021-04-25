#!/usr/bin/env python

import argparse
import sys

from src.classes.TweepyClient import TweepyClient
from src.helpers.Printer import Printer
from src.helpers.HelpStrings import HelpString

class TwitCLI(object):
    twitter = None

    def __init__(self):
        self.twitter = TweepyClient()

        parser = argparse.ArgumentParser(
            description=HelpString.get_main_string("main_description"),
            usage=HelpString.get_main_string("help_usage"),
        )
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def show(self):
        printer = Printer()
        table = printer.asTable('Timeline Tweets')
        table = printer.addColumn(table, ["User","Tweets"])

        tweets = self.twitter.getTweets()
        for tweet in tweets:
            table = printer.addRow(table, tweet)

        table = printer.print(table)


if __name__ == "__main__":
    TwitCLI()