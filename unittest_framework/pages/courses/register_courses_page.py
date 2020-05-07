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
    _all_courses = "row course-list list"
    _enroll_button = "enroll-button"
    _cc_num = "//*[@class='CardNumberField-input-wrapper']/span/input"
    _cc_exp = "//*[@name='exp-date']"
    _cc_cvv = "//*[@name='cvc']"
    _postal = "//*[@name='postal']"
    _submit_enroll = "confirm-purchase"
    _enroll_error_message = "//*[@class = 'payment-error-box only-on-mobile']/span"

    #4578 4562 5643 9173
    #12/22
    #123
    #641

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        listOfCourse = self.getElementList(self._all_courses,'class')
        self.elementClick(element=listOfCourse[0])

    def enterCardNum(self, num):
        self.sendKeys(num,self._cc_num,'xpath')

    def enterCardExp(self, exp):
        self.sendKeys(exp, self._cc_exp, 'xpath')

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, self._cc_cvv, 'xpath')

    def enterPincode(self, pincode):
        self.sendKeys(pincode, self._postal, 'xpath')

    def clickEnrollSubmitButton(self):
        self.elementClick(element=self._submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv, pin):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPincode(pin)

    def enrollCourse(self, num="", exp="", cvv=""):
        
        Hint:

    • Click
    on
    the
    enroll
    button
    • Scroll
    down
    • Enter
    credit
    card
    information
    • Click
    Enroll in course
    button

    def verifyEnrollFailed(self):
        Verify
        the
        element
        for error    message is displayed, not just present.
You	need	to	verify	if	it	is	displayed
Hint:	The	element	is	not	instantly	displayed,	it	take	some	time
to	display
You	need	to	wait	for	it	to	display