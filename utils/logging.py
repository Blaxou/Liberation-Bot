import datetime
import time

class Logger(object):
    """A custom logger"""
    def __init__(self, filename):

        self.filename = filename

    def log(self, type, msg):
        t = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        string = "{} : [{}] {} \n".format(t, type, msg)
        print(string)
        with open(self.filename, "a") as f:
            f.write(string)

    def error(self, msg):
        self.log('ERROR', msg)

    def info(self, msg):
        self.log('INFO', msg)

    def critical(self, msg):
        self.log('CRITICAL', msg)
