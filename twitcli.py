#!/usr/bin/env python

import argparse
import sys

from src.classes.TweepyClient import TweepyClient
from src.helpers.HelpStrings import HelpString

from src.modules.Show import Show

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
        Show(self.twitter);


if __name__ == "__main__":
    TwitCLI()