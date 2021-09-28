from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from password import PASSVAR

driver = webdriver.Firefox()

driver.get("https://tamuengr.emscloudservice.com/web")

# Click sign in button on original website
WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[4]'
                                          '/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/button'))).click()

loginUser = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, 'i0116'))
)

loginUser.send_keys("mihiranpandey@tamu.edu")
loginUser.send_keys(PASSVAR)
