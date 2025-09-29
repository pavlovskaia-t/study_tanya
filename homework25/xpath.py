from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")



signup_button = "//button[text()='Sign up']"
logo = "//header//a[contains(@href, '/')]"
home_button = "//button[text()='Home']"
about_button = "//button[text()='About']"
contacts_button = "//button[text()='Contacts']"
guest_login_button = "//button[text()='Guest log in']"
signin_button = "//button[text()='Sign In']"
play_button = "//button[text()='Смотреть']"
video = "//*[@id='movie_player']//video"
main_title = "//h1[text()='Do more!']"
main_text = "//p[contains(text(), 'With the help')]"
h2_title = "//h2[text()='Log fuel expenses']"
h2_text = "//p[contains(text(), 'Keep track')]"
h2_instructions = "//*[@id='aboutSection']//p[1]"
text_instructions = "//*[@id='aboutSection']//p[2]"
fuel_expenses_img = "//*[@id='aboutSection']//img"
instructions_img = "//*[@id='aboutSection']//div[2]//img"
about_section = "//*[@id='aboutSection']"
contacts_section = "//*[@id='contactsSection']"
mail_hillel_link = "/div[@id='contactsSection']//a[text()='ithillel.ua']"
contacts_link = "//div[@id='contactsSection']//a[text()='support@ithillel.ua']"