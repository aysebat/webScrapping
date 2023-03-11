#Copied for the web scraping dynamic data
#main.py will going to use for the scaraping the Login info
from selenium import webdriver
import time

######################################
#add this line for your local computer
#from selenium.webdriver.chrome.service import Service
#service = Service('\pathof_the _choromeDriver') #you should downlond from web and make the place the absolute path in Service
######################################


def get_driver():

  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")  #start browser as maximized
  options.add_argument(
    "disable-dev-shm-usage")  #to avoid issues with a browser on a linux
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  #instantiate driver
  #dont need to execute the path because we are uisng repl
  driver = webdriver.Chrome(options=options)
  ######################################
  #add this line for your local computer
  #use this driver options in your local computer
  #driver = webdriver.Chrome(service=service, options=options)
  ######################################

  driver.get("http://automated.pythonanywhere.com")
  return driver


def clean_text(text):
  """Extract only the temprature fro tetx"""
  output = float(text.split(": ")[1])
  return output


def main():
  """Extract the text from http://automated.pythonanywhere.com"""
  #load the page
  driver = get_driver()
  #for staying on the page for two second we need to sleep
  time.sleep(2)
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)


print(main())