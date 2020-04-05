from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

MIN  = 0
login_url = "https://www.bestbuy.ca/identity/en-ca/signin?tid=111111111"
item_url = "https://www.bestbuy.ca/en-ca/product/1111111"
cart_url = "https://www.bestbuy.ca/en-ca/basket"

UID = str('email')
UPASSWORD = str('password')
CVV = int(1111)

class BestBuyPurchase():
    def __init__(self):
        self.status = 0
        self.uid = UID
        self.upw = UPASSWORD
        self.cvv = CVV
        print('###Open Chrome Browser###')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get(login_url)
        print('###Login Starts###')
        time.sleep(3)
        username = self.choose('//*[@id="email"]')
        username.send_keys(self.uid)
        password = self.choose('//*[@id="password"]')
        password.send_keys(self.upw)
        login = self.choose('//*[@id="signIn"]/div/button/span')
        login.click()
        time.sleep(5)

    def refresh_until_available(self):
        print('###Refresh and check availability###')
        self.driver.get(item_url)
        while True:
            time.sleep(1)
            addcart_btn = self.choose('//*[@id="test"]/button[@class="button_1XJDJ primary_1csTK addToCartButton_1DQ8z addToCartButton regular_1e4gO"]/span/div/span')
            if addcart_btn:
                addcart_btn.click()
                break
            time.sleep(8)
            self.driver.refresh()
        time.sleep(2)

    def enter_cart(self):
        print('###Enter Cart###')
        self.driver.get(cart_url)
        time.sleep(3)

    def check_out(self):
        print('###Checking out###')
        checkout = self.choose('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/section/section[2]/div[2]/div/a/span/span')
        checkout.click()
        time.sleep(2)

    def fill_in_cvv(self):
        print('###Finally!!###')
        cvv = self.choose('//*[@id="cvv"]')
        cvv.send_keys(self.cvv)

    def place_order(self):
        po_button = self.choose('//*[@id="posElement"]/section/section[1]/button/span')
        po_button.click()

    def choose(self, seletor):
        try:
            wait = WebDriverWait(self.driver, 5)
            choice = wait.until(EC.element_to_be_clickable((By.XPATH, seletor)))
            return choice
        except TimeoutException as e:
            print("Time out!")
            return None
        except Exception:
            print("Not found!")
            return None


if __name__ == '__main__':
    con = BestBuyPurchase()
    con.login()
    con.refresh_until_available()
    con.enter_cart()
    con.check_out()
    con.fill_in_cvv()
    con.place_order()
