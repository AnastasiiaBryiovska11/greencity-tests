import pip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#anastasiia.b.second@gmail.com
#1111Nnn/

BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

if __name__ == "__main__":


    oprions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=oprions)
    driver.implicitly_wait(1)

    driver.maximize_window()
    driver.get(BASE_URL)
    print(driver.title)

    wait = WebDriverWait(driver, 10)

    sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
    sign_in_button = driver.find_element(By.CSS_SELECTOR, sign_in_selector)

    sign_in_button.click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button_xpath = "//button[@class='greenStyle']"
    sign_in_button = driver.find_element(By.XPATH, sign_in_button_xpath)
    assert sign_in_button.is_displayed(), "Sign in button is not displayed"
    email_input.send_keys("anastasiia.b.second@gmail.com")
    password_input.send_keys("1111Nnn/")
    sign_in_button.click()

    events_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Події')]"))
    )

    events_button.click()

    time_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//mat-label[normalize-space()='Час події']"))
    )

    time_button.click()

    future_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Майбутні']/span"))
    )
    future_option.click()

    past_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Завершені']/span"))
    )
    past_option.click()

    driver.find_element(By.TAG_NAME, "body").click()

    clean_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Очистити ']"))
    )

    clean_button.click()

    where_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//mat-label[normalize-space()='Де?']"))
    )

    where_button.click()

    driver.find_element(By.TAG_NAME, "body").click()

    status_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//mat-label[normalize-space()='Статус']"))
    )

    status_button.click()

    driver.find_element(By.TAG_NAME, "body").click()

    type_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//mat-label[normalize-space()='Тип події']"))
    )

    type_button.click()

    allType_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()=' Всі типи ']"))
    )
    allType_option.click()

    driver.find_element(By.TAG_NAME, "body").click()


    driver.quit()