from datetime import datetime

class emailid():
    def __init__(self, driver):
        self.driver = driver


    email = "RS" + datetime.now().strftime("%Y%m%d%H%M") + "@gmail.com"


def new_email():
    new_email = "RS" + datetime.now().strftime("%Y%m%d%H%M") + "@gmail.com"
    return new_email