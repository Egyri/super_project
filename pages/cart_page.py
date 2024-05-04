from base.base_classs import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# The cart page (asserting brand and price also making screenshot)
class CartPage(Base):

    # Locators
    phone_name = '//div[@class="name_list"]'
    phone_price = '//div[@class="price_block total"]'
    proceed = '//div[@id="buttons"]'

    # Getters
    def get_phone_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_name)))

    def get_phone_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_price)))

    def get_proceed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.proceed)))

    # Actions
    def click_get_proceed(self):
        self.get_proceed().click()
        print('Clicking Proceed button')

    # Methods
    def checking_cart(self):
        self.get_current_url()
        self.assert_brand_in_cart(self.get_phone_name(), 'Samsung Galaxy S24 Ultra, Dual SIM, 12/1TB, 5G, Titanium Black')
        self.assert_brand_in_cart(self.get_phone_price(), '28 999 лей')
        self.click_get_proceed()

