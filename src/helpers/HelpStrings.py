class HelpString:
    main = {
        "main_description": "Twitter CLI Apps to keep in touch your tweets quickly",
        "help_usage": """
        twitcli <command> [<args>]
        
        Commands are able to use :
        show      Show homeline tweets quickly
        tweet     Write a new tweet"""
    }

    show = {
        "show_description": "Show tweets summary quickly",
        ## Arguments help texts
        "arg_me": "Shows your last tweets",
        "arg_username": "Shows specific user's tweets",
        "arg_count": "Number of tweets to be shown ",
    }

    tweet = {
        "tweet_description": "Write a new tweet",
        ## Arguments help texts
        "arg_m": "Write your message what you like",
    }

    @staticmethod
    def get_main_string(arg_name):
        return HelpString.main.get(arg_name)

    @staticmethod
    def get_show_string(arg_name):
        return HelpString.show.get(arg_name)

    @staticmethod
    def get_tweet_string(arg_name):
        return HelpString.tweet.get(arg_name)
