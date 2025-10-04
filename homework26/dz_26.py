from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_frame(frame_id, input_id, secret_text):
    frame = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, frame_id))
    )
    driver.switch_to.frame(frame)

    driver.find_element(By.ID, input_id).send_keys(secret_text)
    driver.find_element(By.TAG_NAME, "button").click()

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert alert.text == "Верифікація пройшла успішно!", f"Помилка: {alert.text}"
    alert.accept()

    driver.switch_to.default_content()

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")


check_frame("frame1", "input1", "Frame1_Secret")
check_frame("frame2", "input2", "Frame2_Secret")

print("Обидві верифікації пройшли успішно!")

driver.quit()
