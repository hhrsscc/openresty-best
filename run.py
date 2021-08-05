""" run test """
import time
import logging

def build_logger(logger_name,
                 log_file=None,
                 log_level=logging.WARN,
                 log_format=None):
    """ Build a logger """
    if log_format:
        formatter = logging.Formatter(fmt=log_format)
    else:
        formatter = logging.Formatter(
            fmt='%(name)s - %(asctime)s - %(threadName)s - %(process)d - '
            '%(module)s - %(funcName)s - %(lineno)d - %(levelname)s: \n%(message)s'
        )
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    stream_handle = logging.StreamHandler()
    stream_handle.setLevel(log_level)
    stream_handle.setFormatter(formatter)
    logger.addHandler(stream_handle)

    if log_file:
        file_handle = logging.FileHandler(log_file)
        file_handle.setLevel(log_level)
        file_handle.setFormatter(formatter)
        logger.addHandler(file_handle)
    return logger

if __name__ == "__main__":
    logger = build_logger("run", log_file="run.log", log_level=logging.INFO)
    logger.info("Start")
    time.sleep(30)
    logger.info("End")
