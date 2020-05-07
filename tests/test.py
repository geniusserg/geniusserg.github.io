from Selenium import webdriver  
import time  
from Selenium.webdriver.common.keys import Keys

filename = "/tmp/"+str(time.time())+"_log"
log = open(filename,'w')
print(log, "testing started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://localhost:80/carConfig.htm")
time.sleep(3)
driver.close()
print(log, "site opened")
log.close()