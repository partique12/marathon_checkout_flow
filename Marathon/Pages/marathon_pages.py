from pylenium.driver import Pylenium

from Marathon.Pages.cartPage import CartPage
from Marathon.Pages.homePage import HomePage


class MarathonPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.home = HomePage(py)
        self.cart = CartPage(py)

    def goto(self) -> Pylenium:
        return self.py.visit('https://marathon.ua/uk/')

