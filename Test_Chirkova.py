from selenium import webdriver
from selenium import webdriver
import time

link = 'https://demoqa.com'



browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)
button1 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div')
button1.click()

time.sleep(1)
button2 = browser.find_element_by_xpath('//*[@id="item-1"]')
button2.click()

time.sleep(1)
checkbox = browser.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/label')
checkbox.click()

time.sleep(1)
button3 = browser.find_element_by_xpath('//*[@id="item-2"]')
button3.click()

time.sleep(1)
radioButt1 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]')
radioButt1.click()

time.sleep(1)
radioButt2 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]')
radioButt2.click()

time.sleep(1)
browser.quit()