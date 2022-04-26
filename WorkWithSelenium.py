from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()

driver.get("https://www.google.com")
print(driver.title + " | " + driver.current_url)

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")
search_box.send_keys("Selenium")
wait1 = WebDriverWait(driver, 10)
search_button = wait1.until(EC.element_to_be_clickable(search_button))
search_button.click()
print(driver.title + " | " + driver.current_url)

driver.implicitly_wait(0.5)

driver.get("https://icad.org/")
element_button = driver.find_element(By.ID, "menu-item-59")
element_button.click()
print(driver.title + " | " + driver.current_url)

driver.quit()