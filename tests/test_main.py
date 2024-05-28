"""
2024 (с) 
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


def test_smoke():
    """
    SMK-1. Smoke test
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.get("https://sushi-uat.ru/")

    buttonList = browser.find_elements(By.CSS_SELECTOR, "div.t776__btn-wrapper > a")
    for button in buttonList:
        if button.text == "Заказать":
            button.click()
            link = browser.find_element(By.PARTIAL_LINK_TEXT, "Добавить в корзину")
            x = browser.find_element(By.CSS_SELECTOR, "div.t-popup__close")
            x.click()

    return

