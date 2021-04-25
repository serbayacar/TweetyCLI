from configparser import ConfigParser

class Config():

    path='./src/configs'
    section= 'Keys'

    def getConfig(self, key):
        config = ConfigParser()
        config.read(self.path)

        return config.get(self.section, key)