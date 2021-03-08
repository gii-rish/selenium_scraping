from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

path = "C:\Program Files (x86)\chromedriver.exe"
url = "https://www.amazon.in/"

driver = webdriver.Chrome(path)
driver.get(url)

driver.maximize_window()

searchBar = driver.find_element_by_id("twotabsearchtextbox")
searchBar.clear()
searchBar.send_keys("nike shoes")
searchBar.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
driver.find_element_by_id("a-autoid-14-announce").click()

driver.implicitly_wait(3)
driver.find_element_by_link_text("50% Off or more").click()

driver.implicitly_wait(2)
driver.find_element_by_xpath("//span[text()='Sort by:']").click()
driver.find_element_by_link_text("Avg. Customer Review").click()

driver.find_element_by_xpath("//span[data-component-id()='185']").click()

driver.implicitly_wait(3)
# driver.close()