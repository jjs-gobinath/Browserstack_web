import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from values import strings
class GoogleOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        # self.driver.get(strings.base_url)
        self.driver = webdriver.Chrome()
        self.driver.get(strings.base_url)

    def test_google_search_page(self):
        driver = self.driver

        window_before = driver.window_handles[0]
        print(window_before)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()