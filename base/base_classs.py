from datetime import datetime


class Start:
    # Open browser with website for test
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.smart.md/ru/'
        self.driver.get(self.url)
        self.driver.maximize_window()


class Base:

    def __init__(self, driver):
        self.driver = driver

    # Method to get url
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ', get_url)

    # Method to assert brand
    def assert_brand(self, word, result):
        value_word = word.text
        assert value_word == result
        print('This your choice -', value_word)

    # Method to assert brand in cart
    def assert_brand_in_cart(self, word, result):
        value_word = word.text
        assert value_word == result
        print('The value is correct -', value_word)


# Method to take screenshot
class ScreenShot:
    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self):
        now_date = datetime.now().strftime('%Y,%m,%d,%H,%M')
        name_screen = 'screen' + now_date + '.png'
        self.driver.save_screenshot('./screens/' + name_screen)
        print('Added', name_screen, 'screenshot')
