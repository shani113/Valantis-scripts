import time
from selenium.webdriver.common.by import By


class login_form():
    signIn_button = "//*[@id='root']/div[1]/div[3]/div/div/div[2]/button[1]"
    signIn_InputF = "/html/body/div/div[1]/div[3]/div/div/form/div[1]/input"
    SignIn_pass_ = "/html/body/div/div[1]/div[3]/div/div/form/div[2]/input"
    SignIn_B_C = "/html/body/div/div[1]/div[3]/div/div/form/div[3]/button[2]"

    def __init__(self, driver):
        self.driver = driver

    def setuserbutton(self):
        element = self.driver.find_element(By.XPATH, self.signIn_button)
        element.click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.signIn_InputF).clear()
        self.driver.find_element(By.XPATH, self.signIn_InputF).send_keys(username)

    def setPassword(self, password):
        password_field= self.driver.find_element(By.XPATH, self.SignIn_pass_)
        password_field.clear()
        self.driver.find_element(By.XPATH, self.SignIn_pass_).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.SignIn_B_C).click()
