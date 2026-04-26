import pip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

if __name__ == "__main__":
    #print(pip.__version__)
    #print(pip.__file__ )


    oprions = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=oprions)
    driver.implicitly_wait(1)

    driver.maximize_window()
    driver.get(BASE_URL)
    print(driver.title)

    wait = WebDriverWait(driver, 10)

    regist_selector = ".header_sign-up-link > .header_sign-up-btn"
    #regist_button = driver.find_element(By.CSS_SELECTOR, regist_selector)

    regist_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, regist_selector))
    )

    regist_button.click()

    email_input = driver.find_element(By.ID, "email")
    user_name_input = driver.find_element(By.ID, "firstName")
    password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "repeatPassword")

    regist_button_xpath = "//button[@class='greenStyle']"


    regist_button = driver.find_element(By.XPATH, regist_button_xpath)
    assert regist_button.is_displayed(), "Sign up button is not displayed"

    email_input.send_keys("teest@test.com")
    user_name_input.send_keys("Test")
    password_input.send_keys("tEst/1234")
    confirm_password_input.send_keys("tEst/1234")
    regist_button.click()

    try:
        error_message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-show"))
        )

        print("User already exists")
        print(error_message.text)

        sleep(2)

        close_button_xpath = "//img[@alt='close button']"
        close_button = driver.find_element(By.XPATH, close_button_xpath)
        assert close_button.is_displayed(), "Close button is not displayed"
        close_button.click()
    except:
        print("No error message — user probably created")

    wait = WebDriverWait(driver, 3)
    driver.quit()