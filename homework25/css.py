from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


signup_button = "button.hero-descriptor_btn"
logo = "a.header_logo"
home_button = "a.header-link.-active"
about_button = "button[appscrollto='aboutSection']"
contacts_button = "button[appscrollto='contactsSection']"
guest_login_button = "button.header-link.-guest"
signin_button = "button.header_signin"
hero_title = "h1.hero-descriptor_title"
hero_text = "p.hero-descriptor_descr"
video_frame = "div.hero-video iframe.hero-video_frame"
about_h2_1 = "div#aboutSection .about-block:nth-child(1) .about-block_title"
about_text_1 = "div#aboutSection .about-block:nth-child(1) .about-block_descr"
about_img_1 = "div#aboutSection .about-block:nth-child(1) img.about-picture_img"
about_h2_2 = "div#aboutSection .about-block:nth-child(2) .about-block_title"
about_text_2 = "div#aboutSection .about-block:nth-child(2) .about-block_descr"
about_img_2 = "div#aboutSection .about-block:nth-child(2) img.about-picture_img"
contacts_section = "div#contactsSection"
contacts_h2 = "div#contactsSection h2"
contacts_link_ithillel = "div#contactsSection a[href='https://ithillel.ua']"
contacts_link_support = "div#contactsSection a[href^='mailto:']"
