from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_classs import Base


# Assert product after all filters and adding in cart
class AddProduct(Base):
    # Locators
    word = '//div[@class="custom_product_title"]'
    price = '//span[@class="regular"]'
    add_product = '//div[@class="custom_product_tools"]'
    open_cart = '//div[@class="cart_block"]'

    # Getters
    def get_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_add_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product)))

    def get_open_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_cart)))

    # Actions
    def click_get_add_product(self):
        self.get_add_product().click()
        print('Adding product in cart ')

    def click_get_open_cart(self):
        self.get_open_cart().click()
        print('Opening cart')

    # Methods
    def adding_product(self):
        self.assert_brand(self.get_word(), 'Samsung Galaxy S24 Ultra, Dual SIM, 12/1TB, 5G, Titanium Black')
        self.assert_brand(self.get_price(), '28 999 лей')
        self.click_get_add_product()
        self.click_get_open_cart()
