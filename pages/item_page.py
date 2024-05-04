import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from base.base_classs import Base


# Page to select all filters for choosing a phone
class UpdateFilter(Base):

    # Locators
    price = '//div[@class="noUi-connect"]'
    company = '//div[@data-search-facet-value="samsung"]'
    color_down = '//*[@id="search_facet_metaf_culoare"]/div[1]/label'
    color = '//*[@id="search_facet_metaf_culoare"]/div[2]/div[1]/div[1]'
    model_down = '//*[@id="search_facet_metaf_model_telefon"]/div[1]/label'
    model = '//*[@id="search_facet_metaf_model_telefon"]/div[2]/div[1]/div[1]/label'
    memory_down = '//*[@id="search_facet_metaf_memorie_interna"]/div[1]/label'
    memory = '//*[@id="search_facet_metaf_memorie_interna"]/div[2]/div/div[1]/label'
    accum_down = '//*[@id="search_facet_metaf_capacitate_acumulator"]/div[1]/label'
    accum = '//*[@id="search_facet_metaf_capacitate_acumulator"]/div[2]/div/div/label'
    ram_down = '//*[@id="search_facet_metaf_memorie_ram"]/div[1]/label'
    ram = '//*[@id="search_facet_metaf_memorie_ram"]/div[2]/div/div/label'
    screen_size_down = '//*[@id="search_facet_metaf_diagonala_(inch)"]/div[1]/label'
    screen_size = '//*[@id="search_facet_metaf_diagonala_(inch)"]/div[2]/div/div/label'
    processor_down = '//*[@id="search_facet_metaf_producator_procesor"]/div[1]/label'
    processor = '//*[@id="search_facet_metaf_producator_procesor"]/div[2]/div/div/label'

    # Getters
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = None

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_company(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.company)))

    def get_color_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_down)))

    def get_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_model_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model_down)))

    def get_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model)))

    def get_memory_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory_down)))

    def get_memory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory)))

    def get_accum_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accum_down)))

    def get_accum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accum)))

    def get_ram_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_down)))

    def get_ram(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram)))

    def get_screen_size_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size_down)))

    def get_screen_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_size)))

    def get_processor_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_down)))

    def get_processor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor)))

    # Actions
    def page_up(self):
        self.actions = ActionChains(self.driver)
        self.actions.send_keys(Keys.ARROW_UP*7)
        self.actions.perform()

    def switch_get_price(self):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.get_price())
        self.actions.click_and_hold()
        self.actions.move_by_offset(20, 0)
        self.actions.perform()
        print('Manage price filter')

    def click_company(self):
        self.get_company().click()
        print('Manage company filter')

    def click_color_down(self):
        self.get_color_down().click()

    def click_color(self):
        self.get_color().click()
        print('Manage color filter')

    def click_get_model_down(self):
        self.get_model_down().click()

    def click_get_model(self):
        self.get_model().click()
        print('Manage model filter')

    def click_get_memory_down(self):
        self.get_memory_down().click()

    def click_get_memory(self):
        self.get_memory().click()
        print('Manage memory filter')

    def click_get_ak_down(self):
        self.get_accum_down().click()

    def click_get_ak(self):
        self.get_accum().click()
        print('Manage accum filter')

    def click_get_ram_down(self):
        self.get_ram_down().click()

    def click_get_ram(self):
        self.get_ram().click()
        print('Manage ram filter')

    def click_get_screen_size_down(self):
        self.get_screen_size_down().click()

    def click_get_screen_size(self):
        self.get_screen_size().click()
        print('Manage screen size filter')

    def click_get_processor_down(self):
        self.get_processor_down().click()

    def click_get_processor(self):
        self.get_processor().click()
        print('Manage processor filter')

    # Methods
    def select_the_filters(self):
        self.switch_get_price()
        self.click_company()
        time.sleep(3)
        self.click_color_down()
        self.click_color()
        self.click_get_model_down()
        self.click_get_model()
        time.sleep(3)
        self.click_get_memory_down()
        self.click_get_memory()
        self.click_get_ak_down()
        self.click_get_ak()
        self.click_get_ram_down()
        self.click_get_ram()
        time.sleep(3)
        self.click_get_screen_size_down()
        self.click_get_screen_size()
        self.click_get_processor_down()
        self.click_get_processor()
        self.page_up()
        self.get_current_url()
