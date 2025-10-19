from selenium.webdriver.common.by import By

class MainPageLocators:
    SIGNUP_BTN = (By.CSS_SELECTOR, "[data-testid='menu-signup'], a[href*='signup'], button[data-testid='signup']")
    LOGIN_BTN  = (By.CSS_SELECTOR, "[data-testid='menu-login'], a[href*='login'], button[data-testid='login']")

