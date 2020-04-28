from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.activeCases = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//*[@id='#dashboard']/div[2]/div/span")))
        self.discharged = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//*[@id='#dashboard']/div[3]/div/span")))
        self.death = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//*[@id='#dashboard']/div[4]/div/span")))
        self.migrated = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//*[@id='#dashboard']/div[5]/div/span")))
        self.stateLevelStatus = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "outerlink")))

    def validate_activeCases(self):
        assert self.activeCases.is_displayed()

    def validate_discharged(self):
        assert self.discharged.is_displayed()

    def validate_death(self):
        assert self.death.is_displayed()

    def validate_migrated(self):
        assert self.migrated.is_displayed()

    def clickStatus(self):
        self.stateLevelStatus.click()