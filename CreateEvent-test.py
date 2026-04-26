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

    #sleep(4)

    events_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Події')]"))
    )

    #sleep(2)
    events_button.click()
    #sleep(1)

    create_events_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.secondary-global-button.m-btn"))
    )

    create_events_button.click()

    title_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname='title']"))
    )
    duration_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "mat-select[formcontrolname = 'duration']"))
    )


    title_input.send_keys("testIvent2")

    duration_button.click()
    #sleep(1)

    option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = ' 1 день ']"))
    )

    option.click()
    #sleep(1)

    type = wait.until(
        EC.element_to_be_clickable((By.XPATH, " //span[text() = ' Соціальний ']"))
    )

    type.click()
    #sleep(1)

    invite_button = wait.until(
    EC.presence_of_element_located((By.XPATH, "//mat-label[normalize-space()='Запросити']"))
    )


    invite_button.click()
    #sleep(1)

    invite_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Друзів']"))
    )
    invite_option.click()
    #sleep(1)

    editor = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ql-editor"))
    )

    editor.click()
    editor.send_keys("Мій текстnnnnn")

    startTime_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname = 'startTime']"))
    )

    driver.execute_script("arguments[0].click();", startTime_button)

    options = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option"))
    )

    options[0].click()



    finishTime_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[formcontrolname = 'finishTime']"))
    )

    driver.execute_script("arguments[0].click();", finishTime_button)

    finishTime_button.clear()
    finishTime_button.send_keys("23:00")

    #sleep(2)

    place_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//label[text()=' Онлайн ']"))
    )

    place_button.click()

    place_text_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Додайте посилання')]/ancestor::mat-form-field//input"))
    )


    place_text_button.send_keys("https://www.google.com/")

    public_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-global-button.submit-buttons"))
    )

    public_button.click()


    print("Create Enent")
    sleep(3)
    driver.quit()