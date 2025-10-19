from selenium.webdriver.common.by import By

class RegisterPageLocators:
    FIRSTNAME    = (By.CSS_SELECTOR, "#signupName, input[name='name']")
    LASTNAME     = (By.CSS_SELECTOR, "#signupLastName, input[name='lastName'], input[name='surname']")
    EMAIL        = (By.CSS_SELECTOR, "#signupEmail, input[type='email']")
    PASSWORD     = (By.CSS_SELECTOR, "#signupPassword, input[name='password']")
    REPASSWORD   = (By.CSS_SELECTOR, "#signupRepeatPassword, input[name='repeatPassword']")
    POLICY_CHECK = (By.CSS_SELECTOR, "#signupAgree, input[type='checkbox'][name*='agree'], input[type='checkbox']")
    REGISTER_BTN = (By.CSS_SELECTOR, "form[action*='signup'] button[type='submit'], button[type='submit']")
    SUCCESS_TOAST= (By.CSS_SELECTOR, ".toast-success, .alert-success, .notification-success")

