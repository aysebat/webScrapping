from selenium import webdriver

def get_driver():

  #set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized") #start browser as maximized
  options.add_argument("disable-dev-shm-usage") #to avoid issues with a browser on a linux
  options.add_argument("no-sandbox") 
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  #instantiate driver
  #dont need to execute the path because we are uisng repl
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())