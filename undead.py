""" run undead """
import os
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

def undead(process_name, start_cmd, logger):
    detect_cmd = "ps aux | grep %s" % process_name
    sys_output = ""
    with os.popen(detect_cmd) as fr:
        sys_output = fr.read()
    logger.info("sys_output: %s" % sys_output)
    if "run.py" not in sys_output:
        logger.warn("Restart %s by %s" % (process_name, start_cmd))
        with os.popen(start_cmd) as fr:
            pass

if __name__ == "__main__":
    logger = build_logger("undead", log_file="undead.log", log_level=logging.INFO)
    while 1:
        undead("run", "python run.py", logger)
        sleep(10)
