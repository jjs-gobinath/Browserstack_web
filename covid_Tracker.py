from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from pandas import DataFrame


# BROWSERSTACK_URL = 'https://gobinathr1:NFsD7sZqn3RfMNcvkScq@hub-cloud.browserstack.com/wd/hub'
# desired_cap = {
#
#     'os': 'Windows',
#     'os_version': '10',
#     'browser': 'Chrome',
#     'browser_version': '80',
#     'name': "Bstack-[Python] Web Test",
#     'browserstack.local': True
# }
# driver = webdriver.Remote(
#     command_executor=BROWSERSTACK_URL,
#     desired_capabilities=desired_cap
# )

#DataFrame
data = {'STATE NAME': [],
        'TOTAL CONFIRMED': [],
        'CURED/DISCHARGED/MIGRATED': [],
        'DEATH': []
        }
new_frame = DataFrame(data)
driver = webdriver.Chrome()
driver.get("https://www.mygov.in/covid-19")
first_result = ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_class_name("outerlink"))
first_link = driver.find_element_by_class_name("outerlink")
first_link.click()

handles = driver.window_handles
size = len(handles)

for x in range(size):
    driver.switch_to.window(handles[x])
    print(driver.title)
    if driver.title == "COVID19 STATEWISE STATUS | MyGov.in" :
        list_of_state = driver.find_elements_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div")
        no_of_states = len(list_of_state)
        print(no_of_states)
        for sTamilnadu in range(no_of_states):
            try:
                stateName = driver.find_element_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(sTamilnadu) + "]/div/div/div/div[1]/div[2]/div").text
                total_confirmed = driver.find_element_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(sTamilnadu) + "]/div/div/div/div[2]/div[2]/div").text
                discharged = driver.find_element_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(sTamilnadu) + "]/div/div/div/div[3]/div[2]/div").text
                death = driver.find_element_by_xpath("//*[@id='node-287111']/div/div[8]/div/div[2]/div[" + str(sTamilnadu) + "]/div/div/div/div[4]/div[2]/div").text
                # DataFrame
                new_frame = new_frame.append({'STATE NAME': stateName, 'TOTAL CONFIRMED': total_confirmed,'CURED/DISCHARGED/MIGRATED': discharged, 'DEATH': death}, ignore_index=True)
            except NoSuchElementException:
                pass
print(new_frame)
driver.quit()