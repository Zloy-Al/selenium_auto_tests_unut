from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_choice(browser):
    browser.get(link)
    browser_lang = browser.find_element(By.TAG_NAME, "html").get_attribute("lang")
    button_text = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")
        )).text
    lng = {"es": "Añadir al carrito",
           "fr": "Ajouter au panier",
           "ru": "Добавить в корзину",
           "de": "In Warenkorb legen",
           "en-gb": "Add to basket"}

    assert lng[browser_lang] in button_text

