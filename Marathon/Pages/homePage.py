from pylenium.driver import Pylenium


class HomePage:
    def __init__(self, py: Pylenium):
        self.py = py

    def add_to_cart(self):
        self.py.wait(use_py=True).sleep(1)
        self.py.get("#onesignal-slidedown-cancel-button").click()
        self.py.get('div[data-id^="1265517212"]').hover()
        self.py.get('div[data-id^="1265517212"] svg[class="icon cart"]').click()
        self.py.get('div>label:first-of-type').click()
        self.py.get("button[class='btn_primary btn_add_cart']").click()

    def open_cart(self):
        self.py.get('.btn_success').click()