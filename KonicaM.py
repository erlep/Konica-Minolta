#
# Konica Minolta bizhub 552 - REST Api - Selenium automation
# KonicaM.py - stáhne Pdf z boxu číslo 8 - https://10.0.8.54
#
# Selenium with Python - https://selenium-python.readthedocs.io/
# Selenium Webdriver with Python: Tutorial with Example - https://www.guru99.com/selenium-python.html

# ChromeDriver - WebDriver for Chrome - https://sites.google.com/a/chromium.org/chromedriver/getting-started
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup
import time

# selenium - How to bypass the message-“your connection is not private” on non-secure page using Selenium? - https://is.gd/7NDpuF
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome('d:/Utils/chromedriver/chromedriver.exe', options=options)
# napred hl. stranka a pak /wcd/box.xml
driver.get('https://10.0.8.54')
driver.get('https://10.0.8.54/wcd/box.xml')

# driver.find_element_by_class_name()
# driver.find_element_by_css_selector
# driver.find_element_by_id('8_LNK').click()
# driver.find_element_by_link_text("8").click()
# driver.find_element_by_name()
# driver.find_element_by_tag_name()
# driver.find_element_by_xpath('//*[@id="F_UOU_OPE"]/option[text()="Download to PC"]').click()
# time.sleep(1)  # Let the user actually see something!

# Python Selenium: Click a href=“javascript:()” - https://is.gd/Adawdj
driver.execute_script("html_f.execBoxLogin('F_UOU','User','8','','_NotRelayAuthOn');")
time.sleep(1)  # Let the user actually see something!

# How to select a drop-down menu option value using Selenium - Python - https://is.gd/7bX67l
select = Select(driver.find_element_by_id('F_UOU_OPE'))
time.sleep(1)  # Let the user actually see something!
# Now we have many different alternatives to select an option.
# select.select_by_index(4)

# # select.select_by_visible_text("Download to PC")
select.select_by_value('FileDownload')  # Pass value as string
# Klik na "Changes the display"
driver.find_element_by_xpath('//*[@id="F_UOU_FD"]/div[2]/table[3]/tbody/tr/td[2]/input').click()
time.sleep(2)  # Let the user actually see something!

# Klik na vyber dokumentu
driver.find_element_by_id('F_UOU_CHK1').click()
time.sleep(1)  # Let the user actually see something!
driver.execute_script("html_f.SetDocumentNumber('F_UOU','1','1'); html_f.ClearErr();html_f.SetDocSelect('F_UOU','1','1','User','FileDownload')")
time.sleep(2)  # Let the user actually see something!

# DownLoad
driver.find_element_by_id('F_UOU_Next0').click()
time.sleep(2)  # Let the user actually see something!
# OK
driver.find_element_by_css_selector('#F_UOU_DOFileDownload > div.buttonarea-layout > input[type=submit]:nth-child(1)').click()
time.sleep(9)  # Let the user actually see something!
# Download
driver.find_element_by_id('btnEXE').click()

# # quit - schchvalne vypnute
# driver.quit()
print('OkDone.')
