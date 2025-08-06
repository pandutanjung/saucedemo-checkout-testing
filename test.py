from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
time.sleep(1)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(1)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

driver.find_element(By.ID, "checkout").click()
time.sleep(1)

driver.find_element(By.ID, "first-name").send_keys("Pandu")
driver.find_element(By.ID, "last-name").send_keys("Tanjung")
driver.find_element(By.ID, "postal-code").send_keys("16119")
driver.find_element(By.ID, "continue").click()
time.sleep(1)

driver.find_element(By.ID, "finish").click()
time.sleep(1)

thank_you_message = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "Thank you for your order!" in thank_you_message, "Checkout gagal!"

print("Test selesai: Checkout berhasil dan halaman Thank You muncul.")

driver.quit()