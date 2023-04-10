import inspect
import logging


class BaseClass:

    def getLogger(self):

        loggername = inspect.stack()[1][3]
        log = logging.getLogger(loggername)

        filehandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        filehandler.setFormatter(formatter)

        log.addHandler(filehandler)  # filehandler object

        log.setLevel(logging.DEBUG)

        return log