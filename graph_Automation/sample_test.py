from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class AutomatingGraph():
    cdrv = webdriver.Chrome()
    cdrv.get("http://referencewebapp.qaautomation.net/svg.php");
    cdrv.implicitly_wait(15)
    print("Sleeping for 10 sec")
    time.sleep(5)
    VioletePartElm = cdrv.find_elements_by_css_selector("div#svgchart div svg g:nth-child(4) g")
#        cdrv.find_element_by_css_selector("#svgchart > div > svg > g:nth-child(4) > g:nth-child(1) > text")
    print(len(VioletePartElm))
    print(VioletePartElm[0].find_element_by_css_selector("text").text)
    # except:
    #     print("Error")
    # finally:
    cdrv.quit();