from pandas import DataFrame
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import dataFrame
from values import strings


class StateScreen:

    def __init__(self, driver):
        self.driver = driver
        self.list_of_statePresence = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='node-287111']/div/div[8]/div/div[2]")))
        # self.stateName = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((
        #         By.XPATH, "//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
        #         pos) + "]/div/div/div/div[1]/div[2]/div")))
        # self.total_confirmed = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((
        #         By.XPATH,"//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
        #         pos) + "]/div/div/div/div[2]/div[2]/div")))
        # self.discharged = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((
        #         By.XPATH,"//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
        #         pos) + "]/div/div/div/div[3]/div[2]/div")))
        # self.death = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((
        #         By.XPATH,"//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
        #     pos) + "]/div/div/div/div[4]/div[2]/div")))

    def getStateWiseStatus(self,pos):
        new_frame = DataFrame(dataFrame.data)
        no_of_states = len(self.driver.instance.find_elements_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div"))
        print(no_of_states)
        for sTamilnadu in range(no_of_states):
            try:
                stateName = self.driver.instance.find_element_by_xpath(
                    "//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
                        sTamilnadu) + "]/div/div/div/div[1]/div[2]/div").text
                total_confirmed = self.driver.instance.find_element_by_xpath(
                    "//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
                        sTamilnadu) + "]/div/div/div/div[2]/div[2]/div").text
                discharged = self.driver.instance.find_element_by_xpath(
                    "//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
                        sTamilnadu) + "]/div/div/div/div[3]/div[2]/div").text
                death = self.driver.instance.find_element_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(
                    sTamilnadu) + "]/div/div/div/div[4]/div[2]/div").text
                # DataFrame
                new_frame = new_frame.append({'STATE NAME': stateName, 'TOTAL CONFIRMED': total_confirmed,
                                              'CURED/DISCHARGED/MIGRATED': discharged, 'DEATH': death},
                                             ignore_index=True)
            except NoSuchElementException:
                pass
        print(new_frame)