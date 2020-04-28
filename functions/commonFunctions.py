from wDriver import Driver
import selenium.webdriver.support.ui as ui

driver = Driver()


def waitForElement(locatorType, locatorValue):
    switcher={
        'find_by_id':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_id(locatorValue)),
        'find_by_name':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_name(locatorValue)),
        'find_by_xpath':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_xpath(locatorValue)),
        'find_by_link_text':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_link_text(locatorValue)),
        'find_by_partial_link_text':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_partial_link_text(locatorValue)),
        'find_by_tag_name':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_tag_name(locatorValue)),
        'find_by_class_name':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_class_name(locatorValue)),
        'find_by_css_selector':ui.WebDriverWait(driver, 15).until(lambda browser: browser.find_element_by_css_selector(locatorValue))
    }

    func=switcher.get(locatorType,lambda :'Invalid')
    return func()