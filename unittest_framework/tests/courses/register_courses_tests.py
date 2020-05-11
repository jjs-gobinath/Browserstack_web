from pages.courses.register_courses_page import RegisterCoursePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from tests.home import login_tests
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.course = RegisterCoursePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.login("test123@email.com", "123123")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.course.enterCourseName("javascript")
        self.course.selectCourseToEnroll()
        self.course.enrollCourse(num="4578456256439173", exp="1222", cvv="123", pin="641008")
        self.course.verifyEnrollFailed()

