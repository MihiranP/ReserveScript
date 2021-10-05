from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from password import PASSVAR
from time import sleep


def navigateToBooking(PASSVAR):
    # Click sign in button on original website
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[4]'
                                              '/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/button'))).click()
    # Find user and password input
    loginUser = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'i0116'))
    )
    # send User and Pass Data
    loginUser.send_keys("mihiranpandey@tamu.edu")
    loginPass = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'i0118'))
    )
    # input password
    loginPass.send_keys(PASSVAR)
    # Click Next on username prompt
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    # sleep so it doesnt click sign in too early
    sleep(0.5)
    # Click Sign in after entering user name and password
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    # click continue
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div/form[1]'
                                              '/div[1]/fieldset/div[1]/button'))).click()
    # click push for duo
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
    # click create reservation
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "/html/body/form/div[6]/"
                                              "div[1]/ul/li[2]/a/span"))).click()
    # book now button
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/'
                                              'div/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[1]'))).click()


def searchBooking(Date, Time):
    # fill in date booking
    datebook = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="booking-date-input"]')))
    datebook.clear()
    datebook.send_keys(Date)
    # fill in time booking
    timebook = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="start-time-input"]')))
    timebook.clear()
    timebook.send_keys(Time)
    # Search Bookings
    timebook = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[3]/div[3]/div[4]/div[1]/div[2]'
                                              '/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div[2]/button'))).click()


date = input("Enter the date that you want to book (mm/dd/yyyy): ")
time = input("Enter the starting time for your \nbooking (only in intervals of 15 with AM or PM): ")
driver = webdriver.Firefox()
driver.get("https://tamuengr.emscloudservice.com/web")
navigateToBooking(PASSVAR)
searchBooking(date, time)


