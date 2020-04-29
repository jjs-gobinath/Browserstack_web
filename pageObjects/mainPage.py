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
                By.XPATH, strings.mp_activeCases)))
        self.discharged = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, strings.mp_discharged)))
        self.death = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, strings.mp_death)))
        self.migrated = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, strings.mp_migrated)))
        self.stateLevelStatus = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, strings.mp_stateLevelStatus )))

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