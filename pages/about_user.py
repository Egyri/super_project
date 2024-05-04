from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_classs import Base

faker = Faker('en_US')
name = faker.first_name()
last = faker.last_name()
phone = faker.phone_number()
mail = faker.email()


# Fill data about user and selecting few variants for checkout
class AboutUser(Base):
    # Locators
    first_name = '//input[@id="firstname"]'
    last_name = '//input[@id="lastname"]'
    phone_number = '//input[@id="phone"]'
    email_address = '//input[@id="email"]'
    comment = '//textarea[@name="comment"]'
    abx = 'This is Test Automation baby'
    point = '//*[@id="shipping_block_content"]/div/div[3]/div/div[1]/div[1]'
    point_adress = '//div[@class="shipping_block_type"]'
    room = '//a[@data-id="_RDS_"]'
    pay_method = '//img[@src="catalog/view/smartv3/svg/wallet.svg"]'
    send_me = '//img[@src="catalog/view/smartv3/svg/call.svg"]'
    agreement = '//label[@for="confirm_checkbox"]'
    check_out = '//button[@id="checkout_button"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_email_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_address)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.point)))

    def get_point_adress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.point_adress)))

    def get_room(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.room)))

    def get_pay_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_method)))

    def get_send_me(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_me)))

    def get_agreement(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agreement)))

    def get_check_out(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_out)))

    # Actions
    def input_first_name(self,  first_name):
        self.get_first_name().send_keys(first_name)
        print('Filled first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Filled last name')

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Filled phone number')

    def input_email_address(self, email_address):
        self.get_email_address().send_keys(email_address)
        print('Filled email address')

    def input_comment(self):
        self.get_comment().send_keys(self.abx)
        print('Filled comment')

    def click_get_point(self):
        self.get_point().click()
        print('Clicking point')

    def click_get_point_adress(self):
        self.get_point_adress().click()
        print('Clicking point adress')

    def select_get_room(self):
        self.get_room().click()
        print('Selecting room')

    def click_get_pay_method(self):
        self.get_pay_method().click()
        print('Selected cash method')

    def click_get_send_me(self):
        self.get_send_me().click()
        print('Clicking send me')

    def click_get_agreement(self):
        self.get_agreement().click()
        print('Clicking agreement')

    def click_get_check_out(self):
        self.get_check_out().click()
        print('The item added and checked out')

    # Methods
    def fill_data(self):
        self.get_current_url()
        self.input_first_name(name)
        self.input_last_name(last)
        self.input_phone_number(phone)
        self.input_email_address(mail)
        self.input_comment()
        self.click_get_point()
        self.click_get_point_adress()
        self.select_get_room()
        self.click_get_pay_method()
        self.click_get_send_me()
        self.click_get_agreement()
        self.click_get_check_out()




