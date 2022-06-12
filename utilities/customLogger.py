import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="E:\\Edwisely_Automation\\Edwisely_Automation_Project\\Logs\\automation.log",
                            force=True,format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
