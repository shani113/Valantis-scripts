
import time
from PageObjects.loginpage import login_form
from PageObjects.Package import Packages
class Test_002_Package:
    baseURL = "https://develop--valantis-platform.netlify.app/"
    username = "veer1@yopmail.com"
    password = "Zeeshan12"
    verification_pin="111111"

    def testPackage(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.obj = login_form(self.driver)
        self.driver.obj.setuserbutton()
        time.sleep(5)
        self.driver.obj.setUserName(self.username)
        self.driver.obj.setPassword(self.password)
        self.driver.obj.clickLogin()
        self.driver.packageobj=Packages(self.driver)
        self.driver.packageobj.click_package()
        self.driver.packageobj.click_on_plus()
        self.driver.packageobj.click_on_continue_button()
        self.driver.packageobj.setverification_pin()
        self.driver.packageobj.click_on_verify_button()
        self.driver.packageobj.click_on_continue_B()
        self.driver.packageobj.click_on_close()




