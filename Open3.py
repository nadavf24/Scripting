import time
import sys
#import os
import logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import datetime

#fill in this variables
driver_path = 'C:\\Users\\roni2\\Downloads\\chromedriver1'
extension_path = 'C:\\Users\\roni2\\Downloads\\extension_990_71_6_0.crx'


chrome_options = webdriver.ChromeOptions()

def wait_until_browser_loaded(interval, maxTime):
    start_time = datetime.now()
    #elements = []
    while (datetime.now() - start_time).seconds < maxTime:
        time.sleep(interval)
        if browser.title != 'Loading...':
            return
if len(sys.argv) == 1:
	filepath = input('Path for input file: ')
#C:\Users\roni2\Downloads\20.txt
urls = open(filepath)
#urls = urlsFile.readlines() # use this if you want to enter urls in different lines
#urls = urlsFile.read().split(",") # use this if you want to enter comma separated urls.

logging.basicConfig(filename='.\\script.log',filemode='w',level=logging.DEBUG, format='%(levelname)s %(asctime)s %(message)s ')

#chrome_options.add_argument('--load-extension={}'.format(extension_path)) #//run as admin
#chrome_options.add_experimental_option('useAutomationExtension', False)  #//posiable solution for users not in domain

chrome_options.add_extension(extension_path) ###crx of SandBlast Extension
#os.environ["webdriver.chrome.driver"] = driver_path



browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
browser.set_page_load_timeout(60)
titleNumber = 1
for url in urls:
        try:
            time.sleep(3)
            browser.get(("https://www." + url ))
            #print(url)
            time.sleep(1)

            title = browser.title
            if title == "Loading...":
                wait_until_browser_loaded(5, 10)
            if title == "Loading...":
                logging.debug("Title Load" + " - " + str(titleNumber))
                print ("Title Load" + " - " + str(titleNumber))
            else:
                logging.debug(title + " - "+ str(titleNumber))
                print (title + " - "+ str(titleNumber))
            titleNumber +=1
        except TimeoutException as e:
           logging.debug("Timeout")
           print("Timeout")
browser.quit()