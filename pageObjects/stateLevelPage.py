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
            EC.visibility_of_element_located((By.XPATH, strings.sl_list_of_statePresence)))


    def getStateWiseStatus(self,pos):
        new_frame = DataFrame(dataFrame.data)
        no_of_states = len(self.driver.instance.find_elements_by_xpath(strings.sl_no_of_states))

        for pos in range(no_of_states):
            try:
                total_confirmed = self.driver.instance.find_element_by_xpath(strings.sl_total_confirmed.replace('position', str(pos))).text
                stateName = self.driver.instance.find_element_by_xpath(strings.sl_stateName.replace('position', str(pos))).text
                discharged = self.driver.instance.find_element_by_xpath(strings.sl_discharged.replace('position', str(pos))).text
                death = self.driver.instance.find_element_by_xpath(strings.sl_death.replace('position', str(pos))).text
                # DataFrame
                new_frame = new_frame.append({'STATE NAME': stateName, 'TOTAL CONFIRMED': total_confirmed,
                                              'CURED/DISCHARGED/MIGRATED': discharged, 'DEATH': death},
                                             ignore_index=True)
            except NoSuchElementException:
                pass
        print(new_frame)