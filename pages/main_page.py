from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_classs import Start, Base


class MainPage(Start, Base):

    # Locators
    mobile_page = '//a[@href="smartphone"]'

    # Getters

    def get_mobile_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_page)))

    # Actions
    def click_get_mobile_page(self):
        self.get_mobile_page().click()
        print('Select category')

    # Methods
    def chose_category(self):
        self.get_current_url()
        self.click_get_mobile_page()
