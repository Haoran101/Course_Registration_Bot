import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class CourseBot:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        STARS = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"
        self.driver.get(STARS)

    def login_to_stars(self, username, password):
        self.driver.find_element_by_id("UID").send_keys(username)
        self.random_sleep(1)
        self.driver.find_element_by_xpath(u'//input[@value="OK"]').click()
        self.random_sleep(1)
        self.driver.find_element_by_id("PW").send_keys(password)
        self.random_sleep(1)
        self.driver.find_element_by_xpath(u'//input[@value="OK"]').click()
        self.random_sleep(2)

    def load_plan(self, plan_number):
        select_plan_ele = None
        while select_plan_ele is None:
            select_plan_ele = self.driver.find_element_by_xpath(u'//select[@name="plan_no"]')
            self.random_sleep(1)
        select_plan = Select(select_plan_ele)
        while not EC.element_to_be_clickable(select_plan_ele):
            self.random_sleep(1)
        select_plan.select_by_value(str(plan_number))
        self.random_sleep(1)
        self.click_button("Load")
        self.random_sleep(1)
        self.answer_alert()
        print("Plan {} is Loaded!".format(plan_number))
        self.random_sleep(3)

    def add_course(self):
        self.click_button("Add (Register) Selected Course(s)")
        self.click_button("Confirm to add course(s)")
        self.random_sleep(5)
        self.click_button("Back to Timetable")

    def click_button(self, button_value, type="input"):
        btn = None
        while btn is None:
            btn = self.driver.find_element_by_xpath(u'//{}[@value="{}"]'.format(type, button_value))
            self.random_sleep(1)
        while not EC.element_to_be_clickable(btn):
            self.random_sleep(1)
        self.random_sleep(3)
        btn.click()
    
    def wait_for_registration(self, register_time):
        register_date = datetime.strptime(register_time, "%Y-%m-%d %H:%M")
        now = datetime.now()
        diff = (register_date - now).total_seconds()
        if diff > 0:
            print("Waiting for Registration at " + register_time)
            time.sleep(diff + 0.1)
            print("Registration starts!")

    def random_sleep(self, max_sleep_seconds):
        sleep_time = random.uniform(0.5, max_sleep_seconds*2)
        time.sleep(sleep_time + 0.5)
    
    def answer_alert(self):
        while not EC.alert_is_present():
            self.random_sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()

