import time
import sys
from os import path
import logging
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import datetime
logging.basicConfig(filename='.\\script.log',level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s ')
import configparser

config = configparser.ConfigParser()

#fill in this variables
#driver_path = 'C:\\Users\\roni2\\Downloads\\chromedriver1'
#filepath =

options = Options()

def wait_until_browser_loaded(interval, maxTime):
    start_time = datetime.now()
    while (datetime.now() - start_time).seconds < maxTime:
        time.sleep(interval)
        if browser.title != 'Loading...':
            return



if os.path.isfile('./config.ini'):
    print('Config File Found')
    logging.info('Config File Found')

else:
    print('No Exisitng Config File')
    logging.info('No Exisitng Config File')
    driver_path = input('Path for chromedriver: ')
    driver_path = driver_path.strip('\'"')
	filepath = input('Path for input file: ')
    filepath = filepath.strip('\'"')
    usr_dir = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data')
    config['PATH'] = {
        'CDRIVER_PATH': driver_path ,
        'URLFILE_PATH': filepath ,
        'USRDATA_DIR': usr_dir
    }
    with open('./config.ini','w') as configfile:
		config.write(configfile)

#if len(sys.argv) == 1:
#	filepath = input('Path for input file: ')

config.read('./config.ini')
filepath = config.get('PATH','URLFILE_PATH')
driver_path = config.get('PATH','CDRIVER_PATH')
usr_dir = config.get('PATH','USRDATA_DIR')


urls = open(filepath)
#urls = urlsFile.readlines() # use this if you want to enter urls in different lines
#urls = urlsFile.read().split(",") # use this if you want to enter comma separated urls.


options.add_argument("user-data-dir=" + usr_dir)
options.add_argument("--profile-directory=Default")
options.add_argument("--log-level=3")
#options.add_argument('--load-extension={}'.format(extension_path)) #//run as admin
#options.add_experimental_option('useAutomationExtension', False)  #//posiable solution for users not in domain

#options.add_extension(extension_path) ###crx of SandBlast Extension
#os.environ["webdriver.chrome.driver"] = driver_path

browser = webdriver.Chrome(executable_path=driver_path, options=options)
browser.set_page_load_timeout(60)
titleNumber = 1
for url in urls:
        try:
            time.sleep(5)
            browser.get(("https://www." + url ))
            title = browser.title
            if title == "Loading...":
                wait_until_browser_loaded(5, 10)
            if title == "Loading...":
                print (str(titleNumber) + " - " + "Title Load" + " - " + url.rstrip())
                logging.info(str(titleNumber) + " - " + "Title Load" + " - " + url.rstrip())
            elif title == "Check Point SandBlast":
                category = browser.find_element_by_xpath('//*[@id="categoryNames"]')
                print (str(titleNumber) + " - " +title + " - " + "Category: " + category + url.rstrip())
                logging.info(str(titleNumber) + " - " +title + " - " + "Category: " + category + url.rstrip())
            else:
                print (str(titleNumber) + " - " +title + " - "+ url.rstrip())
                logging.info(str(titleNumber) + " - " +title + " - " + url.rstrip())
                titleNumber +=1
        except TimeoutException as e:
           print(str(titleNumber) + " - " + "Timeout" + " - " + str(e))
           logging.info(str(titleNumber) + " - " + "Timeout" + " - " + str(e))
browser.quit()