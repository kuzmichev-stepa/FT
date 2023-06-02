from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('num', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail(reason="Некорректен по условию задания")), *range(8,10)])
def test_guest_can_add_product_to_basket(browser,num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_messages_on_page()

if __name__ == "__main__":
    pytest.main()