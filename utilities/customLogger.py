import logging
from testCases.conftest import setup

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="E:\\Edwisely_Automation\\Edwisely_Automation_Project\\Logs\\automation.log",
                            force=True,format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def statusValidation(self,status,title,driver):
        if  status == "True":
            self.log= title +" Page Verified "
            return self.log
            assert True
        else:
            self.log= title + " Page Verification Fail "
            return self.log
            self.sc = "".join(title.split())
            self.sc = self.sc.strip()
            self.sc = "".join(filter(str.isalnum, self.sc))
            self.sc = self.sc + ".png"
            print("screeshot img",self.sc)
            driver.save_screenshot(".//Screenshots//" + self.sc)
            assert False
            self.driver.close()

