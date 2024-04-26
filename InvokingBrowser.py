import time

from selenium import webdriver

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
our_url = "https://rahulshettyacademy.com/"
fetched_url = driver.current_url
fetchedd_url = driver.current_url
fetcheddd_url = driver.current_url
fetchedddd_url = driver.current_url




time.sleep(2)