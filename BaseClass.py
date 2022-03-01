import logging

class BaseClass():

    def getlogger(self):

        log = logging.getLogger(__name__)  #helps to tell which test case is failing
        file = logging.FileHandler("logfile.log") #name of log file
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file.setFormatter(format)
        log.addHandler(file)

        log.setLevel(logging.INFO)  #set log level
        return log