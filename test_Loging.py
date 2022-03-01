'''
Logs are very useful in case of failure reports.
It acts as proof and helps you to find the reason of failure of reports.
There are 5 levels of Logs:

'''

import logging
def test_logging():

    log = logging.getLogger(__name__)  #helps to tell which test case is failing
    file = logging.FileHandler("logfile.log") #name of log file
    format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    file.setFormatter(format)
    log.addHandler(file)

    log.setLevel(logging.INFO)  #set log level
    log.debug("I am debugging statement")
    log.info("I am Information")
    log.warning("I am Warning statement")
    log.error("I am an Error")
    log.critical("I am Critical issue")