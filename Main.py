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
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[3]/div[3]/div[4]/div[1]/div[2]'
                                              '/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/div[2]/button'))).click()


def iterateBooking(cappref, floorpref):
    table_id = driver.find_element(By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[3]/div[3]/div[4]/div[1]/'
                                             'div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/table/tbody')
    bookList = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
    for row in range(1, len(bookList)):
        capacity = bookList[row].find_elements(By.TAG_NAME, "td")[7].get_attribute("innerHTML")  # get cap from row
        floor = bookList[row].find_elements(By.TAG_NAME, "td")[5].get_attribute("innerHTML")  # get floor from row

        # Check if available room is meets preferences
        if cappref == capacity and floorpref == floor:
            button = bookList[row].find_elements(By.TAG_NAME, "td")[0]
            button.find_element(By.CLASS_NAME, 'add-to-cart').click()

            # click add button after selecting room
            WebDriverWait(driver, 20).until(
                ec.element_to_be_clickable((By.ID, 'setup--add-modal-save'))).click()

            # once we find a room we want exit loop to check all available rooms
            break


def createReservation():
    # click reservation details
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, "/html/body/form/div[6]/div[2]/div/div/"
                                              "div[3]/div[3]/div[2]/ul/li[3]/a"))).click()
    # click Events details and send keys
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'event-name'))).send_keys("ResBot")

    # click terms and conditions box
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.ID, 'terms-and-conditions'))).click()

    # CLICK THE RESERVE BUTTON
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[2]/div/div/div[3]/'
                                              'div[3]/div[4]/div[3]/div[3]/div/span[2]/button'))).click()


# date = input("Enter the date that you want to book (mm/dd/yyyy): ")
# time = input("Enter the starting time for your \nbooking (only in intervals of 15 with AM or PM): ")
# ppl = input("Enter how many people will be attending: ")
# flr = input("Enter floor preference: ")
date = "10/19/2021"
time = "11:00 AM"
ppl = "4"
flr = "2"
driver = webdriver.Firefox()
driver.get("https://tamuengr.emscloudservice.com/web")
navigateToBooking(PASSVAR)
sleep(0.5)
searchBooking(date, time)
sleep(0.5)
iterateBooking(ppl, flr)
sleep(0.5)
createReservation()



