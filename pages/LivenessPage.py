from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.LivenessPageElements as le
import pages.CommonElements as ce

class LivenessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_close_button(self):
        BasePage.click_elements_by_xpath(self, ce.button_x)
        cl.allure_logs("클릭 X 버튼")
    
    def show_livness_title(self):
        BasePage.is_displayed(self, le.text_liveness)
        cl.allure_logs("라이브니스 타이틀 표시")