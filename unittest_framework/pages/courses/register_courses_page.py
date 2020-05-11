import logging
import utilities.custom_logger as cl
from base.basepage import BasePage


class RegisterCoursePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_box = "search-courses"
    #_course = ""
    _all_courses = "//div[contains(@class,'course-listing-title') and contains(text(),'JavaScript for beginners')]"#xpath
    _enroll_button = "enroll-button"
    _cc_num = "//*[@class='CardNumberField-input-wrapper']/span/input"
    _cc_exp = "//*[@name='exp-date']"
    _cc_cvv = "//*[@name='cvc']"
    _postal = "//*[@name='postal']"
    _submit_enroll = "confirm-purchase"
    _agreement = "agreed_to_terms_checkbox"#ID
    _enroll_error_message = "//*[@class = 'payment-error-box only-on-mobile']/span"

    #4578 4562 5643 9173
    #12/22
    #123
    #641
    #iframe[name = '__privateStripeFrame6']
    #iframe[name = '__privateStripeFrame8']

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def enterCardNum(self, num):
        self.swithToFrame("__privateStripeFrame8")
        ls = list(num)
        for x in ls:
            self.sendKeys(x,self._cc_num, 'xpath')
        self.switchToDefault()

    def enterCardExp(self, exp):
        self.swithToFrame("__privateStripeFrame9")
        self.sendKeys(exp, self._cc_exp, 'xpath')
        self.switchToDefault()

    def enterCardCVV(self, cvv):
        self.swithToFrame("__privateStripeFrame10")
        self.sendKeys(cvv, self._cc_cvv, 'xpath')
        self.switchToDefault()

    def enterPincode(self, pincode):
        self.swithToFrame("__privateStripeFrame11")
        self.sendKeys(pincode, self._postal, 'xpath')
        self.switchToDefault()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._agreement)
        self.elementClick(self._submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv, pin):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPincode(pin)


    def enrollCourse(self, num="", exp="", cvv="", pin=""):
        self.elementClick(self._enroll_button)
        self.webScroll('down')
        self.enterCreditCardInformation(num,exp,cvv,pin)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        self.waitForElement(self._enroll_error_message,'xpath',40,2)
        x = self.getElement(self._enroll_error_message,'xpath')
        print(x.text)