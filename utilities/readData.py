import configparser
import random
import string
from datetime import datetime
from datetime import timedelta

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

    def getCustomStartDateAndTime(self):
        self.now=datetime.now()
        self.now+=timedelta(minutes=2)
        self.startTime=self.now.strftime("%d %b %Y %H:%M:%S")   #07 Jan 2021 00:35:20
        return self.startTime

    def getCustomEndDateAndTime(self):
        self.now=datetime.now()
        self.now+=timedelta(minutes=6)
        self.endTime=self.now.strftime("%d %b %Y %H:%M:%S")   #07 Jan 2021 00:35:20
        return self.endTime






