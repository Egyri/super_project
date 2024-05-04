import time
from selenium import webdriver

from base.base_classs import ScreenShot
from pages.about_user import AboutUser
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.item_page import UpdateFilter
from pages.product_in_cart import AddProduct


def test_buy_product(set_up):

    driver = webdriver.Chrome()
    # Open browser select category for test
    mp = MainPage(driver)
    mp.chose_category()
    # Selecting filters ot result our product
    ip = UpdateFilter(driver)
    ip.select_the_filters()
    # Adding product to cart and asserting brand/price
    pic = AddProduct(driver)
    pic.adding_product()
    # Make screenshot
    sh = ScreenShot(driver)
    sh.screen_shot()
    # Asserting brand/price in cart, making screen
    cp = CartPage(driver)
    cp.checking_cart()
    # Filling data about user, checking out
    au = AboutUser(driver)
    au.fill_data()
    time.sleep(10)
