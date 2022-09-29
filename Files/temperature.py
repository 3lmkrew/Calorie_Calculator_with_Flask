# get temperature from scrapping web
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Temperature:

    def __init__(self, state, city):
        self.state = state
        self.city = city

    def Get(self):
        driver = webdriver.Chrome()
        driver.get("https://www.timeanddate.com/weather/")
        time.sleep(1)
        # find city/place search box and type in city and state
        search_box = driver.find_element(By.CSS_SELECTOR,
                                         "body > div.main-content-div > header > div.fixed > div > form > input")
        search_box.send_keys(self.city + " ", self.state)
        time.sleep(1)
        # find search button and click it
        search_button = driver.find_element(By.CSS_SELECTOR,
                                            "body > div.main-content-div > header > div.fixed > div > form > button")
        search_button.click()
        time.sleep(1)
        # find the temperature and convert to a integer
        temp = driver.find_element(By.CSS_SELECTOR,
                                   "body > div.main-content-div > section.bg--grey.pdflexi-t--small > div > section:nth-child(5) > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.rbi")
        fahrenheit_temp = float(temp.text.split(" ")[0])
        celsius_temp = (fahrenheit_temp - 32) * .5556 # convert from F to C.
        return round(celsius_temp, 2)



# This allows to only run below if you run temperature.py if you import to a different file and run, the below will not run.
if __name__ == "__main__":
    Temp = Temperature("California", "San Fransisco ")
    print(Temp.Get())