from pylenium.driver import Pylenium
from selenium.webdriver.common.keys import Keys


class CartPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def open_checkout(self):
        self.py.get('button[class="btn_primary next_step"]').click()

    def checkout_authorization(self, email=str, password=str):
        self.py.get('a[href="#tab_regular_customer"]').click()
        # enter email and password
        self.py.get("#tab_regular_customer input[name='email']").type(email)
        self.py.get("#tab_regular_customer input[name='password']").type(password)

        # login and start checkout
        self.py.get("div.form_group button[class='btn_primary']").click()

    def checkout_flow(self, first_name=str, last_name=str):
        self.py.get("input[name='recipient_firstname']").type(first_name)
        self.py.get("input[name='recipient_lastname']").type(last_name)

    def checkout_delivery(self):
        self.py.get("span[title='Область']").click()
        self.py.get("input[class='select2-search__field']").type('Харків', Keys.ENTER)
        self.py.get("#ordering > section > div.order_data > div > button").click()
        self.py.wait(use_py=True).sleep(2)  # the only way to fins the next selectors (IDK WHY 0_0)
        self.py.get('#tab_new_address > form > div:nth-child(6) > span > span.selection > span').click()
        self.py.get("body>span>span>span.select2-search.select2-search--dropdown > input").type('Харків')
        self.py.get("body > span > span > span.select2-results >ul > li:nth-of-type(217)").click()
        self.py.wait(use_py=True).sleep(2)  # the only way to find the next selectors (IDK WHY 0_0)
        self.py.get('#tab_new_address > form > div:nth-of-type(5)>div:nth-of-type(2)>label:nth-of-type(1)').click()
        self.py.get('#tab_new_address > form > div:nth-of-type(5)>div>div:nth-of-type(2) > span').click()
        self.py.wait(use_py=True).sleep(2)
        self.py.get('body > span > span > span:nth-of-type(1) > input').type('бакул', Keys.ENTER)
        # self.py.get('body>span>span>span.select2-results>ul>li:nth-of-type(51)').click()
        self.py.get('#ordering > section > div.form_tabs > div > div:nth-child(3) > form > div > label:nth-child(5)').click()
        self.py.get('#ordering > section > div.order_data > div > button').click()






