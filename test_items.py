from selenium.webdriver.common.by import By


def test_guest_should_see_btn_add_to_basket(browser):
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'Кнопка добавления товара в корзину не найдена'
