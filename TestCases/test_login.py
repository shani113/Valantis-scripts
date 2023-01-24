
import time

import pytest

from PageObjects.loginpage import login_form
import pytest

class Test_001_Login:
    baseURL = "https://develop--valantis-platform.netlify.app/"
    username = "veer1@yopmail.com"
    password = "Zeeshan12"
    @pytest.mark.skip(reason="I do not want to run this test case")
    def test_lpagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Valantis":
            assert True
        else:
            assert False


    def testplogin(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.obj = login_form(self.driver)
        self.driver.obj.setuserbutton()
        time.sleep(5)
        self.driver.obj.setUserName(self.username)
        self.driver.obj.setPassword(self.password)
        self.driver.obj.clickLogin()
        time.sleep(5)

