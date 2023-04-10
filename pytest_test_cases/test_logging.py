import logging


def test_logging():

    log = logging.getLogger(__name__)

    filehandler = logging.FileHandler("logfile.log")

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    filehandler.setFormatter(formatter)

    log.addHandler(filehandler)  # filehandler object

    log.setLevel(logging.INFO)
    log.debug("A debug statement is executed")
    log.info("An informative statement is executed")
    log.warning("An warning statement is executed")
    log.error("An error statement is executed")
    log.critical("A critical statement is executed")