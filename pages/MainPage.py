from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.MainPageElements as me

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_main_form_liveness_button(self):
        BasePage.click_elements_by_xpath(self, me.button_liveness)
        cl.allure_logs("클릭 라이브니스 버튼")
    
    def click_main_form_ssa_button(self):
        BasePage.click_elements_by_xpath(self, me.button_ssa)
        cl.allure_logs("클릭 SSA 버튼")
    
    def click_main_form_ssa_switch(self):
        BasePage.click_elements_by_xpath(self, me.switch_ssa)
        cl.allure_logs("클릭 SSA 스위치")