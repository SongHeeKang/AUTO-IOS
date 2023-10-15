import time

from behave import step,given,when,then

from base.BasePage import BasePage
from pages.MainPage import MainPage
from pages.LivenessPage import LivenessPage

class LivnessTest:

    @given("Create the class objects")
    def class_objects(context):
        context.mp = MainPage(context.driver)
        context.bp = BasePage(context.driver)
        context.lv = LivenessPage(context.driver)

    @when("Click on Liveness Button")
    def click_contactform_page(context):
        context.mp.click_main_form_liveness_button()

    @then("Show Liveness")
    def show_contactform_page(context):
        context.lv.show_livness_title()