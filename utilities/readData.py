import configparser
import random
import string

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
        return''.join(random.choice(chars) for x in range(size))


