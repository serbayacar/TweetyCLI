class HelpString:
    main = {
        "main_description": "Twitter CLI Apps to keep in touch your tweets quickly",
        "help_usage": """
        twitcli <command> [<args>]
        
        Commands are able to use :
        show      Show tweets quickly""",
    }

    show = {
        "show_description": "Show tweets summary quickly",
        ## Arguments help texts
        "arg_me": "Shows your tweets",
        "arg_username": "Shows specific user's tweets",
    }

    @staticmethod
    def get_main_string(arg_name):
        return HelpString.main.get(arg_name)

    @staticmethod
    def get_add_string(arg_name):
        return HelpString.add.get(arg_name)

    @staticmethod
    def get_remove_string(arg_name):
        return HelpString.remove.get(arg_name)

    @staticmethod
    def get_show_string(arg_name):
        return HelpString.show.get(arg_name)

    @staticmethod
    def get_generate_string(arg_name):
        return HelpString.generate.get(arg_name)

    @staticmethod
    def get_config_string(arg_name):
        return HelpString.config.get(arg_name)