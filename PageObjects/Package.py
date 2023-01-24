import time
from selenium.webdriver.common.by import By


class Packages():
    click_on_packagepage_xpath = "//*[@id='navbarSupportedContent']/div/div[3]/a"
    click_on_plus_sign_xpath = "//*[@id='root']/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[2]/button[2]"
    click_on_continue_button_xpath = "//*[@id='root']/div[2]/div/div[2]/div[4]/div/div[2]/button"
    verification_pin_xpath = "/html/body/div[3]/div/div/form/div[1]/div[1]/div[1]/input"
    click_on_verify_button_xpath = "/html/body/div[3]/div/div/form/div[3]/button"
    click_on_continue_purchase_button_xpath = "/html/body/div[3]/div/div/form/div/button"
    click_on_close_button = "/html/body/div[3]/div/div/form/div/button"

    def __init__(self, driver):
        self.driver = driver

    def click_package(self):
        time.sleep(10)
        self.driver.maximize_window()
        element = self.driver.find_element(By.XPATH, self.click_on_packagepage_xpath)
        time.sleep(5)
        element.click()
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(5)

    def click_on_plus(self):
        element1 = self.driver.find_element(By.XPATH, self.click_on_plus_sign_xpath)
        element1.click()

    def click_on_continue_button(self):
        element2 = self.driver.find_element(By.XPATH, self.click_on_continue_button_xpath)
        element2.click()

    def setverification_pin(self):
        element3 = self.driver.find_element(By.XPATH, self.verification_pin_xpath)
        element3.send_keys("111111")

    def click_on_verify_button(self):
        element4 = self.driver.find_element(By.XPATH, self.click_on_verify_button_xpath)
        element4.click()

    def click_on_continue_B(self):
        element5 = self.driver.find_element(By.XPATH, self.click_on_continue_purchase_button_xpath)
        element5.click()

    def click_on_close(self):
        element6 = self.driver.find_element(By.XPATH, self.click_on_close_button)
        element6.click()
