import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from pageObjects.mainPage import HomeScreen
from pageObjects.stateLevelPage import StateScreen
from values import strings
from wDriver import Driver
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_activeCases()
        home_screen.validate_discharged()
        home_screen.validate_death()
        home_screen.validate_migrated()

    def test_State_level_status(self):
        driver = self.driver
        home_screen = HomeScreen(self.driver)
        home_screen.clickStatus()
        handles = self.driver.getWindowHandles()
        size = len(handles)
        for x in range(size):
            title = self.driver.getWindowTitle(x)
            if title == strings.tc_title:
                state_screen = StateScreen(self.driver)
                state_screen.getStateWiseStatus(x)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()