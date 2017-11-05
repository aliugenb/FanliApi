# -*- coding: utf-8 -*-
# __author__ = Roger
import time
import os

from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# # get the path of chromedriver
# # chrome_driver_path = r"e:\chromedriver.exe"
# #remove the .exe extension on linux or mac platform
#
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'
chromedriver = '/Users/Roger/Documents/Python/Fanli/Conf/chromedriver'
# create a new Chrome session
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page
# driver.get("http://jsonschema.net/#/")
driver.get("https://www.baidu.com/")
print 111
# get the search textbox
search_field = driver.find_element_by_class_name('.soutu-btn .s_ipt')
search_field.send_keys('aaaa')

# enter search keyword and submit
search_field.send_keys("webdriver")
search_field.submit()



time.sleep(6)
products = driver.find_elements_by_xpath("//a[@class='searchable']")
# get the number of anchor elements found
print "Found " + str(len(products)) + " pages:"

# iterate through each anchor element and
# print the text that is name of the product
for product in products:
    print product.get_attribute('href')

# close the browser window
driver.quit()